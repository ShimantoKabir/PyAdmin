import smtplib
from src.email.EmailService import EmailService
from fastapi import BackgroundTasks
from config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailServiceImp(EmailService):

  host: str = Config.getValByKey("HOST")
  port: int = int(Config.getValByKey("PORT"))
  username: str = Config.getValByKey("UNAME")
  password: str = Config.getValByKey("PASSWORD")
  sender: str = "pyadmin@mail.com"

  def __init__(self, bgTask: BackgroundTasks):
    self.bgTask = bgTask

  def sendMail(self, email: str, otp: str):

    print("password=",self.password)
    print("username=",self.username)
    print("host=",self.host)
    print("port=",self.port)

    html : str = f"""
      <html>
        <body>
          <p>Please use this otp: {otp} to verify you account</p>
        </body>
      </html>
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = "Account verification otp!"
    message["From"] = self.sender
    message["To"] = email

    part = MIMEText(html, "html")
    message.attach(part)

    server = smtplib.SMTP(self.host, self.port)
    server.set_debuglevel(1)
    server.esmtp_features['auth'] = 'LOGIN DIGEST-MD5 PLAIN'
    server.login(self.username, self.password)
    server.sendmail(self.sender, email, message.as_string())
  
  def setAccountVerification(self, email: str, otp: str) -> bool:
    self.bgTask.add_task(self.sendMail, email, otp)
    return True