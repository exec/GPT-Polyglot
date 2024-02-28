import os
import click
import json
from getpass import getpass
from crypto_utils import encrypt_data, decrypt_data

CREDENTIALS_FILE = 'credentials.bin'

def get_api_keys(passphrase):
    try:
        with open(CREDENTIALS_FILE, 'rb') as file:
            encrypted_data = file.read()
        return json.loads(decrypt_data(encrypted_data, passphrase))
    except FileNotFoundError:
        return None
    except Exception as e:
        click.echo(f"Error: {e}")
        return None

def save_api_keys(api_keys, passphrase):
    try:
        encrypted_data = encrypt_data(json.dumps(api_keys), passphrase)
        with open(CREDENTIALS_FILE, 'wb') as file:
            file.write(encrypted_data)
        return True
    except Exception as e:
        click.echo(f"Error: {e}")
        return False

def prompt_for_api_keys():
    openai_key = click.prompt("Enter your OpenAI API key")
    neets_key = click.prompt("Enter your Neets.ai API key")
    return {"openai": openai_key, "neets": neets_key}

def init_credentials():
    passphrase = getpass("Enter a passphrase: ")
    api_keys = prompt_for_api_keys()
    if save_api_keys(api_keys, passphrase):
        click.echo("API keys stored.")
    else:
        click.echo("Failed to store API keys.")

def check_and_init():
    if not os.path.exists('credentials.bin'):
        click.echo("First-time setup.")
        init_credentials()