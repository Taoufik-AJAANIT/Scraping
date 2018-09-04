# This script is a toolbox for using email for the different uses we are going to make of it
#Script for python2
# Sending an email and/or file attachement.
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
def envoi_email(fromaddr = "ttproject@koondal.com",password="13TTproject13",toaddr = "EMAIL ADDRESS YOU SEND TO",subject="SUBJECT OF THE EMAIL",body = "TEXT YOU WANT TO SEND", filename ="NAME OF THE FILE WITH ITS EXTENSION", path_attachment = "path/attachement"):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    if not(filename=="NAME OF THE FILE WITH ITS EXTENSION"):
        attachement = open(path_attachment, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)


    server =  smtplib.SMTP_SSL('auth.smtp.1and1.fr', 465)
    server.login(fromaddr, password)
    text = msg.as_string()
    print(toaddr)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

# Reception d'email
import poplib
from email import parser
def reception_email ():
    pop_conn = poplib.POP3_SSL('pop.1and1.fr')
    pop_conn.user("ttproject@koondal.com")
    pop_conn.pass_("13TTproject13")

    # Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:
    messages = ["\n".join(mssg[1]) for mssg in messages]
    # Parse message intom an email object:
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]

#unit tests
def unit_test_mail_send():

    envoi_email(fromaddr="ttproject@koondal.com", password="13TTproject13", toaddr="taoufik.ajaanit.1@gmail.com",
                subject="hola", body="chakhbarkoum",
                filename="NAME OF THE FILE WITH ITS EXTENSION", path_attachment="path/attachement")


if __name__ == '__main__':
    unit_test_mail_send()
