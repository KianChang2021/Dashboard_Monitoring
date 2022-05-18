import smtplib
import time 
import re
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import make_msgid
from email.message import EmailMessage

UserName = ''
UserPassword = ''
toUser = ['']
Developer = ['']
now = datetime.now()
now_1 = now.strftime("%d_%m_%Y")
name = "Dashboard_"+str(now_1)

def emergency_gmail(note):
    msg = EmailMessage()
    msg['Subject'] = 'AD - Live Monitoring'
    msg['From'] = ''
    msg['To'] = ''

    msg.add_alternative("""\
    <html>
    <head></head>
    <body>
        <b>There is an Emergency Case happen Please check now !!!</b>
        <p>{0}</p>
    </body>
    </html>
    """.format(note), subtype='html')

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(UserName, UserPassword)
    s.sendmail(UserName, Developer, msg.as_string())
    s.quit()

    return True

def gmail(folder,note,status):
    img = folder+".png"
    path = name + "/"+img
    with open(path, 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'AD - '+str(now_1)+ ' Automation Monitoring For Adapter - ' + status
    msg['From'] = ''
    msg['To'] = ''

    text = MIMEText("This is an Automation Notice Result Latest !!! \n"+note)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(img))
    msg.attach(image)

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(UserName, UserPassword)
    s.sendmail(UserName, Developer, msg.as_string())
    s.quit()

    print("Done send Gmail")

def Branch_gmail(note,branch):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = str(branch)+' - '+str(now_1)+ ' Automation Monitoring For Adapter - Fail' 
        msg['From'] = ''
        msg['To'] = ''

        text = MIMEText("Automation "+branch+" Emergency !!! \n"+note)
        msg.attach(text)

        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(UserName, UserPassword)
        s.sendmail(UserName, Developer, msg.as_string())
        s.quit()

        print("Done send Gmail")
    except Exception as ex:
        print(str(ex))

def special_gmail(note,branch):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = str(branch)+' - '+str(now_1)+ ' Automation Monitoring For Adapter - Fail' 
        msg['From'] = ''
        msg['To'] = ''

        text = MIMEText("Automation "+branch+" Emergency - Assigned but no data come in !!! \n"+note)
        msg.attach(text)

        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(UserName, UserPassword)
        s.sendmail(UserName, Developer, msg.as_string())
        s.quit()

        print("Done send SE Gmail")
    except Exception as ex:
        print(str(ex))

def check(): 
    try:
        msg = MIMEMultipart()
        msg['Subject'] = 'Azalea - '+str(now_1)+ ' Automation Monitoring For Adapter - Info' 
        msg['From'] = ''
        msg['To'] = ''

        text = MIMEText("Automation Dailt Check Health mergency - Azalea !!! \n")
        msg.attach(text)

        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(UserName, UserPassword)
        s.sendmail(UserName, Developer, msg.as_string())
        s.quit()

        print("Done send Gmail")
    except Exception as ex:
        print(str(ex))
        
def late_sync_gmail(note,branch):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = str(branch)+' - '+str(now_1)+ ' Automation Monitoring For Adapter - Fail' 
        msg['From'] = ''
        msg['To'] = ''

        text = MIMEText("Automation "+branch+" Warning - Late data sync !!! \n"+note)
        msg.attach(text)

        # s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # s.login(UserName, UserPassword)
        # s.sendmail(UserName, Developer, msg.as_string())
        # s.quit()

        print("Done send late sync Gmail")
    except Exception as ex:
        print(str(ex))

def patient_name(note,branch):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = str(branch)+' - '+str(now_1)+ ' Automation Monitoring For Adapter - Fail' 
        msg['From'] = ''
        msg['To'] = ''

        text = MIMEText("Automation "+branch+" Warning - Patient Name not tally !!! \n"+note)
        msg.attach(text)

        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(UserName, UserPassword)
        s.sendmail(UserName, Developer, msg.as_string())
        s.quit()

        print("Done send patient_name Gmail")
    except Exception as ex:
        print(str(ex))

def service_issue(branch):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = str(branch)+' - '+str(now_1)+ ' Automation Monitoring For Adapter - Fail' 
        msg['From'] = ''
        msg['To'] = ''

        text = MIMEText("Automation "+branch+" Service - Died!!! \n")
        msg.attach(text)

        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(UserName, UserPassword)
        s.sendmail(UserName, Developer, msg.as_string())
        s.quit()

        print("Done service issue Gmail")
    except Exception as ex:
        print(str(ex))


def special_gmail(note,branch):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = str(branch)+' - '+str(now_1)+ ' Automation Monitoring For Adapter - Fail' 
        msg['From'] = ''
        msg['To'] = ''

        text = MIMEText("Automation "+branch+" Emergency - NO data in !!! \n"+note)
        msg.attach(text)

        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(UserName, UserPassword)
        s.sendmail(UserName, Developer, msg.as_string())
        s.quit()

        print("Done send special Gmail")
    except Exception as ex:
        print(str(ex))


if __name__ == "__main__":
    special_gmail("dsadsa","aa")
