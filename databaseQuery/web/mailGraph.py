import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from config import *

username = getUsername()
password = getPassword()

fromaddr = username
toaddr  = getEmail()
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Update on your File! id:'+ getTimeStamp()

res = '\n\n'
critInfoFD = open(PATH_TO_UPLOAD+'crit_stats.txt','r')
for l in critInfoFD:
	res += l
res+='\n'

body = "Hello!\n\nHere are the results of your comparison."+res+"\n\nThanks,\nThe ConSpeciFix Team"
 
postMessage = "\n\n\nThis message is in regards to the file uploaded on "+str(datetime.datetime.fromtimestamp(int(getTimeStamp())/1000.0))+"\nSpecies testing against: "+getSingleSpecies()[0]+"\n\n"

body = body + postMessage

msg.attach(MIMEText(body, 'plain'))


#attach the test graph 
filename = "testGraph.pdf"
attachment = open(PATH_TO_UPLOAD+'testGraph.pdf', "rb") 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

#attach the standard graph 
filename = "hmGraph.png"
attachment = open(PATH_TO_OUTPUT+ str(getSingleSpecies()[0]) + '/hmGraph.png', "rb") 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)


#attach the dressen graph 
filename = "boxPlot.pdf"
attachment = open(PATH_TO_UPLOAD+'boxPlot.pdf', "rb") 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)


#attach the word by word results
filename = "results.txt"
attachment = open(PATH_TO_UPLOAD+'criterion.txt', "rb") 
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

print msg.as_string()
print "all done. With everything!"


