import os
import sys
import hou
import getpass
user = getpass.getuser()
base = hou.hscriptExpression('$HIP')
print(base+'/hip/'+user)