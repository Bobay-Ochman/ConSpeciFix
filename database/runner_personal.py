import os
import sys
import shutil
import clean_files

user_path = sys.argv[1] #path to user's files
user_path = user_path.rstrip('/')+'/'
con_path = user_path+'_conspecifix/'
if os.path.exists(con_path):
	shutil.rmtree(con_path)
con_script_path = con_path+'scripts/'
con_db_path = con_path+'database/'
try:
	os.mkdir(con_path)
except Exception as e:
	print('Dir not made, Error: %s' % e)
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

for f in os.listdir(user_path):
	clean_files.cleanFile(f,user_path,con_db_path+userSpecies+'/genes/')

pathToDatabaseComp = con_script_path+origComponentFolders[len(origComponentFolders)-1]
pathToOldConfig = pathToDatabaseComp+'/config.py'
pathToNewConfig = pathToDatabaseComp+'/new_config.py'

oldConfig = open(pathToOldConfig,'r')
newConfig = open(pathToNewConfig,'w')

for l in oldConfig.readlines():
	if 'PATH_TO_OUTPUT = ' in l:
		l = 'PATH_TO_OUTPUT = "'+con_db_path+'"'
	newConfig.write(l)
os.system('mv '+pathToNewConfig+' '+pathToOldConfig)

os.chdir(pathToDatabaseComp)
print(os.getcwd())
os.remove(pathToDatabaseComp+'/config.pyc')
os.system('chmod 777 *')
os.system('python child_runner.py')

