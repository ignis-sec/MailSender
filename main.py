import smtplib
from email.mime.text import MIMEText


metuSmtpPort = 587
metuSmtpServer = "smtp.metu.edu.tr"
gmailSmtpPort = 587
gmailSmtpServer = "smtp.gmail.com"

def message_parse(filename):
    with open(filename,"r",encoding="utf-8") as f:
        msg = MIMEText(f.read())
        f.close()
    return msg

def email_parse(filename):
    with open("emails.txt","r") as f:
        line = f.read()
        f.close()
def session(uid, pwd, fromAddr, toAddr):
    # msg object has to be recreated in every new session
    msg = message_parse("message.txt")
    msg['Subject'] = "HelloWorld"
    msg['From'] = fromAddr
    msg['To'] = toAddr

   
    smtpObject = smtplib.SMTP(metuSmtpServer, metuSmtpPort)
    smtpObject.ehlo()
    smtpObject.starttls()
    resp = smtpObject.login(uid, pwd)
    if (resp):
        print("Login succesfull")
    else:
        print("Error")
    smtpObject.sendmail(msg['From'], msg['To'], msg.as_string())
    smtpObject.quit()

if __name__ == "__main__":
    uid = ""
    pwd = ""
    fromAddr = ""
    
    with open("emails.txt","r") as file:
        for item in file:
            session(uid,pwd,fromAddr,item)
        file.close()
