import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


EMAIL = "EMAIL"
password = 'PASSWORD'
app_password = "GMAIL APP PASSWORD"
URL = "https://www.amazon.com/Apple-Generation-Cancelling-Personalized-Customizable/dp/B0BDHWDR12/ref=sr_1_3?crid=19I8LO957VMH3&keywords=airpods+pro&qid=1668614622&sprefix=airpods+pro%2Caps%2C221&sr=8-3&ufe=app_do%3Aamzn1.fos.18ed3cb5-28d5-4975-8bc7-93deae8f9840"

header = {
  "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
}


response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.find(name="span", class_="a-offscreen")
price = float(data.get_text().split('$')[1])


def send_email(subject, body, sender, recipients, password):
  msg = MIMEText(body)
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = ', '.join(recipients)
  smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  smtp_server.login(sender, password)
  smtp_server.sendmail(sender, recipients, msg.as_string())
  smtp_server.quit()
  
  
message = f"Airpods Pro Price is Now {price}"
if price < 250:
  subject = "Airpods Price Fallen"
  body = message
  sender = EMAIL
  recipients = [EMAIL]
  send_email(subject, body, sender, recipients, app_password)
  
  
  #Old Version
  # with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
  #   connection.starttls()
  #   connection.login(EMAIL, app_password)
  #   connection.sendmail(
  #     from_addr=EMAIL,
  #     to_addrs=EMAIL,
  #     msg=f"SubjectL: Airpods Pro Price Alert\n\n{message}\n{URL}"
  #   )
  
  
  
  # try:
  #   server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
  #   server.login(EMAIL, password)
  #   server.sendmail(EMAIL, EMAIL, message)
  #   server.quit()
  #   print('ok the email has sent ')
  # except:
  #   print('can\'t send the Email')



