import multiprocessing
import sys
import os

print 'cpu cound:', multiprocessing.cpu_count()
print 'my args:', str(sys.argv)
print 'hello World'

#now do all the things you dream of!
#Don't let your todo list stay memes!

prog = 'concat85.py'

os.chdir('../scripts/')

print 'about to run ' + prog + ' with '+sys.argv[1] + ' '+sys.argv[2]
os.system('python ' + prog + ' ' +sys.argv[1] + ' '+sys.argv[2])
print 'finished! '+ prog + ' with '+sys.argv[1] + ' '+sys.argv[2]