import click
from openai_utils import OpenAIUtils
from audio_utils import play_audio, synthesize_speech

GAME_ROUNDS = 10

def main_game_flow(api_keys, topic, difficulty):
    openai_utils = OpenAIUtils(api_key=api_keys['openai'])
    click.echo(f"Theme: {topic}, Difficulty: {difficulty}")
    for round_number in range(GAME_ROUNDS):
        russian_sentence = openai_utils.chat_completion(f"Generate a short to medium length Russian sentence about {topic}. It should involve {difficulty} difficulty of vocabulary and sentence structure.")
        audio_content = synthesize_speech(russian_sentence, api_keys['neets'])
        if audio_content:
            click.echo(f"Round {round_number + 1}:")
            play_audio(audio_content)
            user_translation = click.prompt("Your translation")
            feedback = openai_utils.chat_completion(f"Grade the translation of: {russian_sentence} -> {user_translation}", role='user')
            click.echo(f"Feedback: {feedback}")
        else:
            click.echo("Failed to synthesize speech.")
