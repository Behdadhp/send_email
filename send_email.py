import smtplib, ssl, time, random

with open("test_email.txt") as f:
    lines = f.readline()
test_email = lines.split(", ")

with open("context.txt", encoding='utf-8') as f:
    context = f.read()

port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "your email"
password = "generate email token with your gmail"
message = context.encode("utf-8")
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for receiver_email in test_email:
        ran_num = random.randint(180,300)
        time.sleep(ran_num)
        server.sendmail(sender_email, receiver_email, message)