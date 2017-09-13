import smtplib
import sys
from config import *
from email.mime.text import MIMEText

# Credentials (if needed)
username = getUsername()
password = getPassword()

fromaddr = username
toaddrs  = getEmail()


message = ''
if(len(sys.argv) == 6):
	if sys.argv[5] == 'error':
		message = 'Hello!\n\nSorry, there was a problem reading the file you uploaded. Please make sure it contains either a zip file with both .gff and .fna files, or a single .fa file. \nIf this continues to be a problem, please reach out to the team at conspecifix@gmail.com'
else:
	message = 'Hello!\n\nWe have some updates for you! Your files for analysis have some information at www.conspecifix.com/uploads/'+getTimeStamp() +'\n\nThis analysis was for ' + str(getCompStrain())+' against species ' +getSingleSpecies()[0]+ '. '

msg = MIMEText(message+'\n\nSincerely,\nThe ConSpeciFix Team')

msg['Subject'] = 'Update on your File!'
msg['From'] = fromaddr
msg['To'] = toaddrs

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, [toaddrs], msg.as_string())
server.quit()