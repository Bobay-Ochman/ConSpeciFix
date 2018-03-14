import datetime
import smtplib
import sys
from config import *
from email.mime.text import MIMEText

# Credentials (if needed)

def sendEmail(messageString):
	username = getUsername()
	password = getPassword()

	fromaddr = username
	toaddrs  = getEmail()

	postMessage = "\n\n\nThis message is in regards to the file uploaded on "+str(datetime.datetime.fromtimestamp(int(getTimeStamp())/1000.0))+"\nSpecies testing against: "+getSingleSpecies()[0]+"\nEddited file name: "+getCompStrain()

	msg = MIMEText("Hello!\n\n"+messageString+'\n\nSincerely,\nThe ConSpeciFix Team'+postMessage)

	msg['Subject'] = 'Update on your File! id:'+ getTimeStamp()
	msg['From'] = fromaddr
	msg['To'] = toaddrs

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, [toaddrs], msg.as_string())
	server.quit()