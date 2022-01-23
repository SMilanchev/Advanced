import smtplib, ssl

gmail_username = 'python.test.exercise@gmail.com'
gmail_password = 'TestUser123'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_username, gmail_password)


def send_mail(message):
    message["From"] = gmail_username
    message["To"] = gmail_username
    message["Subject"] = "CPU and Memory report"

    server.sendmail(gmail_username, gmail_username, message.as_string())



