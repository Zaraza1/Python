#tukjhhrmqckbficq


from email.message import EmailMessage


email_sender = "piotr@gmail.com"    #here provide your email
email_password = "abcde"            #here provide your password (!!!security risk delete after use!!!)
import ssl
import smtplib

email_receiver = "ko3ak3paga@gmail.com"

subject = "I works!"
body = "email sent!"
em = EmailMessage()
em["From"] = email_sender
em["To"]= email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:smtp.login(email_sender, email_password)
smtp.sendmail(email_sender, email_receiver, em.as_string())


def password():         
    "asdfgg"                        #here provide your password (!!!security risk delete after use!!!)