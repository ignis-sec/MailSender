import smtplib
import argparse
from email.mime.text import MIMEText

metuSmtpPort = 587
metuSmtpServer = "smtp.metu.edu.tr"
gmailSmtpPort = 587
gmailSmtpServer = "smtp.gmail.com"


def message_parse(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        msg = MIMEText(f.read())
        f.close()
    return msg


def html_parse(fileName):
    with open(fileName,"r",encoding="utf-8") as f:
        html = f.read()

    return html

def session(uid, pwd, fromAddr, toAddr,isHtml):
    # msg object has to be recreated in every new session
    msg = message_parse("message.txt")
    msg['Subject'] = "HelloWorld"
    msg['From'] = fromAddr
    msg['To'] = toAddr
    if(isHtml):
        html = html_parse("htmlMail.txt")
        html2 = MIMEText(html,'html')
        msg.attach(html)


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

    parser = argparse.ArgumentParser()
    parser.add_argument("uid", help="User id --which will be e+first 5 digits of school number--")
    parser.add_argument("pwd", help="User password ")
    parser.add_argument("fromAddr", help="Sender's email")

    args = parser.parse_args()
    uid = args.uid
    pwd = args.pwd
    fromAddr = args.fromAddr


    with open("emails.txt", "r") as file:
        for item in file:
            session(uid, pwd, fromAddr, item,0)
        file.close()
