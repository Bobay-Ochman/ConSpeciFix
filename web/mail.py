import smtplib
import sys
from config import *
from email.mime.text import MIMEText

# Credentials (if needed)
username = 'ConSpeciFix@gmail.com'
password = 'helloW0rldHowAreYou'

fromaddr = 'ConSpeciFix@gmail.com'
toaddrs  = 'brian.e2014@gmail.com'



message = ''
if sys.argv[5] === 'error':
	message = 'Hello!\nSorry, there was a problem reading the file you uploaded. Please make sure it contains either a zip file with both .gff and .fna files, or a single .fa file. \nIf this continues to be a problem, please reach out to the team at conspecifix@gmail.com'
else:
	message = """Hello!
We have some updates for you! Your files for analysis have some information at www.conspecifix.com/uploads/"""+getTimeStamp() +""" 

This analysis was for """ + getCompStrain()+' against species ' +getSingleSpecies()+ '. '

msg = MIMEText(message+"""

Sincerely,
The ConSpeciFix Team""")

msg['Subject'] = 'Update on your File!'
msg['From'] = fromaddr
msg['To'] = toaddrs

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, [toaddrs], msg.as_string())
server.quit()