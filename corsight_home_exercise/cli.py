import click
from corsight_home_exercise.bash_operation import BashOperations
from corsight_home_exercise.os_operations import OsOperations

# note: the cli function won't be invoked of none of the subcommands were used
# if CORSIGHT_ID_ENV should be set on a simple --help call, add the `invoke_without_command=True` to the group decorator
@click.group()
@click.option('--corsight_id', type=int, default=1)
def cli(corsight_id):
    '''
    for any command you may add --help \n
    for example: \n
        main.py call-script --help
    '''
    OsOperations().set_env_var('CORSIGHT_ID', corsight_id)

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

@cli.command()
def flip_coin():
    click.echo(BashOperations().flip_a_coin())
