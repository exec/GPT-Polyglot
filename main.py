import click
from credentials import get_api_keys, check_and_init
from game_utils import main_game_flow
from getpass import getpass

def main():
    check_and_init()
    passphrase = getpass("Enter passphrase: ")
    api_keys = get_api_keys(passphrase)
    if api_keys:
        topic = click.prompt("Enter a theme", default="daily life")
        difficulty = click.prompt("Choose difficulty (easy, medium, hard)", default="easy")
        main_game_flow(api_keys, topic, difficulty)
    else:
        click.echo("Failed to unlock vault.")

if __name__ == '__main__':
    main()
