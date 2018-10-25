import os
import sys
import shutil
import clean_files


import argparse
parser = argparse.ArgumentParser(description="The personal comparison mode for the ConSpeciFix comparison process. www.conspecifix.com/")
parser.add_argument('path_to_comparison', metavar='PATH', type=str,
                    help='path to directory containing .fa files')
parser.add_argument('-t', nargs='?', help='Max# of threads. Defaults to # cores',type=int, dest='threads')

args = parser.parse_args()


print("""
Please site:
Bobay LM, Ochman H. Biological species are universal across life's domains.
Genome Biol Evol. 2017. doi: 10.1093/gbe/evx026.

starting...""")

user_path = args.path_to_comparison #path to user's files
user_path = user_path.rstrip('/')+'/'
con_path = user_path+'_conspecifix/'
if os.path.exists(con_path):
	try:
		shutil.rmtree(con_path)
	except Exception as e:
		print "Could not remove old path: %s" % e
try:
	os.mkdir(con_path)
except Exception as e:
	print('Dir not made, Error: %s' % e)

con_script_path = con_path+'scripts/'
con_db_path = con_path+'database/'
try:
	os.mkdir(con_db_path)
except Exception as e:
	print('Dir not made, Error: %s' % e)


#location of the current set of scripts:
dir_path = os.path.dirname(os.path.realpath(__file__))
origComponentFolders = dir_path.split('/')
componentFolders = origComponentFolders[:len(origComponentFolders)-1]
#this should give us a path to the conspecifix folder
scripts_path = '/'.join(componentFolders)

# copy the scripts into the script folder
try:
    shutil.copytree(scripts_path, con_script_path)
except shutil.Error as e:
    print('Directory not copied. Error: %s' % e)

userSpecies = 'User_spec'
try:
	os.mkdir(con_db_path+userSpecies)
except Exception as e:
	print('Dir not made, Error: %s' % e)
try:
	os.mkdir(con_db_path+userSpecies+'/genes/')
except Exception as e:
	print('Dir not made, Error: %s' % e)

os.remove(con_script_path+'selected_species.txt')
os.remove(con_script_path+'species.txt')

fd = open(con_script_path+'selected_species.txt','w')
fd.write(userSpecies+'\t30\n')
fd.close()
fd = open(con_script_path+'species.txt','w')
fd.write(userSpecies+'\t30\n')
fd.close()

print "cleaning files..."
for f in os.listdir(user_path):
	if '_conspecifix' not in f:
		clean_files.cleanFile(f,user_path,con_db_path+userSpecies+'/genes/')

pathToDatabaseComp = con_script_path+origComponentFolders[len(origComponentFolders)-1]
pathToOldConfig = pathToDatabaseComp+'/config.py'
pathToNewConfig = pathToDatabaseComp+'/new_config.py'

oldConfig = open(pathToOldConfig,'r')
newConfig = open(pathToNewConfig,'w')

for l in oldConfig.readlines():
	if 'PATH_TO_OUT = ' in l:
		l = 'PATH_TO_OUT = "'+con_db_path+'"'
	if 'MAX_THREADS' in l:
		if(args.threads != None):
			l = 'MAX_THREADS = '+str(args.threads)+'\n'
	newConfig.write(l)
newConfig.close()
oldConfig.close()
os.system('mv '+pathToNewConfig+' '+pathToOldConfig)

os.chdir(pathToDatabaseComp)
# print("CWD:\n"+os.getcwd()+"\n")
os.system('chmod 777 *')
# print 'Removing:\n'+pathToDatabaseComp+'/config.pyc\n'
os.system('rm '+pathToDatabaseComp+'/config.pyc')
print "calling launcher..."
os.system('sh '+pathToDatabaseComp+'/child_launcher.sh')

