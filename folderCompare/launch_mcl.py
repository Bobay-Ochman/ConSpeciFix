import os
from config import *

os.system(MCL_PATH+' ' + PATH_TO_MAT + 'input.txt --abc -I 1.2')
os.system('mv  out.input.txt.I12 ' + PATH_TO_MAT)