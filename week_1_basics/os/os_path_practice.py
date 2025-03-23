import os

test_path = os.path.commonpath([os.getcwd(), os.path.abspath('../../../')])

print(os.getcwd())
print(os.path.abspath('../os'))
print(os.path.basename(os.path.abspath('../os')))

# Common path part in all paths in the list
print( os.path.commonpath([os.getcwd(), os.path.abspath('../../../')]) )

# analog of stat() syscall on Unix-based OS
print(os.stat(test_path))

print(os.path.exists('test/test1.txt'))
print(os.path.exists('test/test2.txt'))

print(os.path.isfile('test2.txt'))

print(os.fspath(test_path)) # file system repr of path