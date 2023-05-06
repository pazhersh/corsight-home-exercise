import subprocess

class BashOperations():
    def run_script(self, script_path, args=''):
        result = subprocess.run(f'sh {script_path} {args}', shell=True, capture_output=True)
        return result.stdout or result.stderr
