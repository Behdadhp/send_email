import smtplib, ssl

with open("test_email.txt") as f:
    lines = f.readline()
test_email = lines.split(", ")

with open("context.txt") as f:
    context = f.read()


port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "your email address"
password = "generate your own app password"
message = context.encode("utf-8")
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for receiver_email in test_email:
        server.sendmail(sender_email, receiver_email, message)