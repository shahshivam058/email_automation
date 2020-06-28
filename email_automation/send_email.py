# import smtp library smtp= simple mail transfer protocol
import smtplib
from mail_info import *
from email.mime.text import MIMEText
import email.utils

def brodcast_email():
    for recipeant_name,recipeant_email in zip(recipeant_names,recipeant_emails):
        message = MIMEText(email_text,"html")
        message.add_header("Content-Type","text/html")
        print (message)
        message["To"] = email.utils.formataddr((recipeant_name,recipeant_email))
        message ["From"] = email.utils.formataddr((sender_name,sender_email))
        message ["Subject"] = "Not spame open me"
        print(message.as_string())
        print("sending email")
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,recipeant_email,message.as_string())
        server.quit()
        print("\n email sent \n")

brodcast_email()