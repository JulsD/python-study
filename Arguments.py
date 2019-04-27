import sys
import os

l = len(sys.argv)

if l > 1:
    print('Arguments : ' + str(sys.argv[1:]))
else:
    print('Arguments NOT provided')

os.system('dir')
sys.exit(2)