import subprocess

class BashOperations():
    def run_script(self, script_path, args=''):
        result = subprocess.run(f'sh {script_path} {args}', shell=True, capture_output=True)
        return result.stdout or result.stderr

    def flip_a_coin(self):
        try:
            result = int(self.run_script('src/scripts/flip_a_coin.sh'))
            
            if result == 0:
                return 'One'
            if result == 1:
                return 'Two'
            
        except:
            pass
        
        return 'something went wrong'