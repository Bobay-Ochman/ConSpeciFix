import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from config import *

 
username = 'ConSpeciFix@gmail.com'
password = 'helloW0rldHowAreYou'

fromaddr = 'ConSpeciFix@gmail.com'
toaddr  = 'brian.e2014@gmail.com'
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Update on your File!"
 
body = "Hello!\nHere are the results of your comparison.\n\nThanks,\nThe ConSpeciFix Team"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "gno1.pdf"
attachment = open(PATH_TO_UPLOAD+'gno1.pdf', "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()