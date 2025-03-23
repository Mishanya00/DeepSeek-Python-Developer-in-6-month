import os
import sys 

print('User:', os.getlogin())
print('PID:', os.getpid())
print('PPID:', os.getppid())

print(os.name) # nt = windows
print(sys.platform)
# print(os.uname()) uname exists only on Unix

print(sys.getfilesystemencoding())

print(type(os.environ))
print(os.environ['APPDATA']) # get env variable value
print(os.getenv('APPDATA')) # uses environ for mapping

print(' - - - - - - - - - - exec paths - - - - - - - - - - ')
for p in os.get_exec_path():
    print(p)
print(' - - - - - - - - - - exec paths - - - - - - - - - - ')


# os.walk:

print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
for path,folders,files in os.walk(os.getcwd()):
    print('PATH:', path)
    print('FOLDERS:', ', '.join(folders))
    print('FILES:', ', '.join(files))
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')