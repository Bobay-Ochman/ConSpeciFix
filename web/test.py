import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
username = 'ConSpeciFix@gmail.com'
password = 'helloW0rldHowAreYou'

fromaddr = 'ConSpeciFix@gmail.com'
toaddr  = 'brian.ellis@austin.rr.com'
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Update on your File!"
 
body = "Hello!\n\nHere are the results of your comparison.\n\nThanks,\nThe ConSpeciFix Team\n\n"
 
msg.attach(MIMEText(body, 'plain'))


#attach the test graph 
filename = "MusicTheory.txt"
attachment = open('/Users/Admin/Desktop/MusicTheory.txt', "rb") 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

#attach the standard graph 
filename = "Todo.txt"
attachment = open('/Users/Admin/Desktop/Todo.txt', "rb") 
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

