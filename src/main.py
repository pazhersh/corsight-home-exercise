import click
from os_operations import OsOperations

@click.group()
def cli():
    pass

@cli.command()
def get_env_vars():
    '''get-env-vars'''
    for key, value in OsOperations().get_env_vars().items():
        click.echo(f'{key}={value}')

@cli.command()
@click.argument('key')
def get_env_var(key):
    '''get-env-var <KEY>'''
    click.echo(OsOperations().get_env_var(key))

if __name__ == '__main__':
    cli()