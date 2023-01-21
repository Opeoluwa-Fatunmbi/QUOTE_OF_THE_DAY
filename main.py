import smtplib, random
from email.mime.text import MIMEText

# list of quotes
quotes = ["The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
          "The only way to do great work is to love what you do. - Steve Jobs",
          "The purpose of our lives is to be happy. - Dalai Lama",
          "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
          "Happiness is not something ready made. It comes from your own actions. - Dalai Lama"]

# choose random quote
quote = random.choice(quotes)

# recipient email addresses
recipients = ['example1@gmail.com', 'example2@gmail.com', 'example3@gmail.com']

# sender email address and password
sender = 'example@gmail.com'
password = 'yourpassword'

# create the message
msg = MIMEText(quote)
msg['Subject'] = 'Daily Quote'
msg['From'] = sender

# connect to the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)

# send the message to all recipients
for recipient in recipients:
    msg['To'] = recipient
    server.sendmail(sender, recipient, msg.as_string())

# close the server connection
server.quit()
