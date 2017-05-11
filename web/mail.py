import smtplib
from config import *
from email.mime.text import MIMEText

# Credentials (if needed)
username = 'ConSpeciFix@gmail.com'
password = 'helloW0rldHowAreYou'

fromaddr = 'ConSpeciFix@gmail.com'
toaddrs  = 'brian.e2014@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

msg = MIMEText("""Hello!
We have some information for you at at wwww.ConSpeciFix.com/uploads/"""+getTimeStamp()+"""

Sincerely,
The ConSpeciFix Team""")

msg['Subject'] = 'Update on your File!'
msg['From'] = fromaddr
msg['To'] = toaddrs

server.sendmail(fromaddr, [toaddrs], msg.as_string())
server.quit()