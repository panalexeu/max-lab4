import click
from rich import print

from file import (
    read,
    write
)
from feistel import (
    feistel_encr,
    feistel_decr
)


@click.group
def cli():
    pass


@cli.command('encr')
@click.option('--verbose', default=False, help='Prints avalanche effect')
def encr(verbose):
    """Encrypt text provided in text.txt with Feistel cipher. Cipher will be located in text.encr.txt"""

    text = read('files/text.txt')
    res = feistel_encr(text, verbose)
    write('files/text.encr.txt', res)


@cli.command('decr')
def decr():
    """Decrypt text provided in text.encr.txt with Feistel cipher"""

    text = read('files/text.encr.txt')
    res = feistel_decr(text)
    click.secho(f'text: {res}', fg='cyan')


if __name__ == '__main__':
    cli()
