from email.message import EmailMessage
import ssl
import smtplib
import sqlite3
email_sender = 'mahmudjanovzohidbek10@gmail.com'
email_password = "qbvw acom fsby fasu"
email_reciever = "mahmudjanovzohidbek7@gmail.com"

subject = " Check out my new video"
body = '''
I've just published my new article. check it out!

/** just checking a new function of my application **/
'''
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
res = cur.execute("SELECT email FROM user_information")

emails = res.fetchall()
for i in emails:
    email_reciever = ''.join(map(str,i))
   
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context ) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())