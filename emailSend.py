import smtplib
from email.mime.text import MIMEText
from email.header import Header
import PythonFiles


mail_sender = 'emailgymbot@gmail.com'
mail_receiver = 'adiskahovsky@gmail.com'
username = 'emailgymbot@gmail.com'
password = 'Bot12345678'
server = smtplib.SMTP('smtp.gmail.com:587')

f = open('myfile.txt','r')
subject = 'Отчеты по показателям'
body = f.read()
f.close()
msg = MIMEText(body,'plain','UTF-8')
msg['Subject'] = Header(subject,'UTF-8')

server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(mail_sender,mail_receiver,msg.as_string())
server.quit()
