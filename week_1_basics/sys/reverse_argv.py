import sys

argvs = []

for i in range(len(sys.argv)):
    argvs.append(sys.argv[len(sys.argv)-i-1])

for arg in argvs:
    print(arg, end=', ')
    