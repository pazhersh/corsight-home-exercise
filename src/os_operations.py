import subprocess
import os

class OsOperations():
    def read_disk_stats(self, disk_path):
        raise('not implemented yet')

        stats = statvfs = os.statvfs(disk_path)
        return stats
    
    def set_env_var(self, key, value):
        if os.name == 'posix':  # if is in linux
            exp = f'export {key}="{value}"' # TODO: test via docker or something
        if os.name == 'nt':  # if is in windows
            exp = f'setx {key} "{value}"'
        subprocess.Popen(exp, shell=True).wait()
    
    def get_env_vars(self):
        return dict(os.environ)
    
    def get_env_var(self, key):
        return os.getenv(key)
    
OsOperations().get_env_vars()