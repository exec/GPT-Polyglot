# GPT Polyglot

## Overview

This project is a proof-of-concept command-line game designed to leverage the power of AI for language learning in an interactive and engaging manner. It integrates OpenAI's GPT-4 for generating conversation prompts and translations, and Neets.ai's multilingual text-to-speech (TTS) capabilities to provide users with an immersive learning experience. The game focuses on translating spoken Russian sentences to English, aiming to improve the user's listening comprehension and translation skills through a series of tailored conversational exercises.

## Caveats

This project isn't thoroughly tested and is rough around the edges. It currently just demonstrates the basic logic flow I'm going for with this concept. I hope to refine this as time goes on, potentially turning it into a useful utility for polyglots in any combination of languages. For now it's exclusively Russian-to-English as I'm learning Russian myself.

## Features

- **Interactive Gameplay**: Offers a unique way to practice language skills by translating spoken words from Russian to typed English.
- **Tailored Difficulty Levels**: Users can choose their difficulty level and subject of choice, making it suitable for learners at various stages of proficiency with different vocabulary needs.
- **Real-Time Feedback**: Incorporates OpenAI's GPT-4 to generate sentences and provide immediate feedback on translations, facilitating a conversational learning approach.
- **High-Quality Speech Synthesis**: Utilizes Neets.ai's TTS technology to synthesize speech in Russian, enhancing listening comprehension skills.
- **Secure Credential Management**: Safely stores API keys using encrypted files, ensuring user data protection.

## Technologies Used

- **OpenAI GPT-4**: For generating conversational prompts and grading translations. [OpenAI](https://openai.com)
- **Neets.ai Text-to-Speech**: For converting text prompts into high-quality spoken audio in multiple languages. [Neets.ai](https://neets.ai)
- **Python**: The entire project is developed in Python, utilizing libraries such as `click` for CLI interactions, `cryptography` for secure key storage, and `pygame` for audio playback.

## Getting Started

To get started with this game, clone the repository, and install the required dependencies. You'll need Python 3.8 or later and pip installed on your system. Follow the setup instructions detailed in the project to configure your API keys securely.

## Usage

Run the game from the command line, and follow the interactive prompts to start practicing. You can select the theme and difficulty level for each session, allowing for a personalized learning experience.

## Contributions

This project is open for contributions. Whether it's adding new features, improving the codebase, or fixing bugs, your input is welcome. Please feel free to fork the repository and submit pull requests.

## Credits

- **Co-authored by**: [dh](https://github.com/exec) and GPT-4 Turbo by [OpenAI](https://openai.com).
- **Powered by**: OpenAI's GPT-4 Turbo for intelligent content generation and translation grading, Neets.ai for highly-affordable multilingual text-to-speech synthesis.

## License

This project is licensed under GPLv3 as detailed in the [license file](/LICENSE.md).