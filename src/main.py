import click
from bash_operation import BashOperations
from os_operations import OsOperations

@click.group()
def cli():
    '''
    for any command you may add --help
    for example:
        main.py call-script --help
    '''
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

@cli.command()
@click.argument('script_path')
@click.option('--arguments', '-a')
def call_script(script_path, arguments):
    '''call-script <SCRIPT_PATH> [-a|--argument]'''
    result = BashOperations().run_script(script_path, arguments)
    click.echo(result)

if __name__ == '__main__':
    cli()
