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


if __name__ == "__main__":

    uid = ""
    pwd = ""
    msg = message_parse("message.txt")
    msg['Subject'] = "HelloWorld"
    msg['From'] = ""


    smtpObject = smtplib.SMTP(metuSmtpServer, metuSmtpPort)
    smtpObject.ehlo()
    smtpObject.starttls()
    resp = smtpObject.login(uid, pwd)
    if (resp):
        print("Login succesfull")

    else:
        print("Error")

    with open("emails.txt","r") as file:
        for item in file:
            msg['To'] = item
            smtpObject.sendmail(msg['From'],msg['To'],msg.as_string())

        file.close()
    smtpObject.quit()
