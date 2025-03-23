import os
import shutil
from zipfile import ZipFile
from datetime import datetime

'''
Write a program that creates a backup of a specified directory by archiving it into a `.zip` file.'
'''

def archive_directory(source, dest):
    '''Archives source directory'''

    if not os.path.isdir(source):
        print('Error: Source path is not a folder or not exist!')
        return False
    if not os.path.isdir(dest):
        print('Error: Destination path is not a folder or not exist!')
        return False
    
    curr_time = datetime.now()
    timestamp = curr_time.strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = dest + '\\' + 'backup_{}'.format(timestamp) + '.zip'

    with ZipFile(backup_filename, 'w') as fzip:
        for path, _, files in os.walk(source):
            for file in files:
                fzip.write(path + '\\' + file)
    return True

archive_directory('test', 'test2')