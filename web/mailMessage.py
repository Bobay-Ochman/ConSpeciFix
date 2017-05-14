import smtplib
import sys
from config import *
from email.mime.text import MIMEText

# Credentials (if needed)

def sendEmail(messageString):
	username = 'ConSpeciFix@gmail.com'
	password = 'helloW0rldHowAreYou'

	fromaddr = 'ConSpeciFix@gmail.com'
	toaddrs  = getEmail()

	msg = MIMEText("Hello!\n\n"+messageString+'\n\nSincerely,\nThe ConSpeciFix Team')

	msg['Subject'] = 'Update on your File!'
	msg['From'] = fromaddr
	msg['To'] = toaddrs

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, [toaddrs], msg.as_string())
	server.quit()