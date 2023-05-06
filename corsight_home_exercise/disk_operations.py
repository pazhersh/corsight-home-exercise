import shutil

class DiskOperations:
    def read_disk_stats(self, mount_path = '/'):
        total, used, free = shutil.disk_usage(mount_path)
        
        return {
            'Total': f'{total / (2**30)} GiB',
            'Used': f'{used / (2**30)} GiB',
            'Free': f'{free / (2**30)} GiB'
        }