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
  sender: str = Config.getValByKey("SENDER")

  def __init__(self, bgTask: BackgroundTasks):
    self.bgTask = bgTask

  def sendMail(self, email: str, html: str, subject: str):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = self.sender
    message["To"] = email

    part = MIMEText(html, "html")
    message.attach(part)

    server = smtplib.SMTP(self.host, self.port)
    server.set_debuglevel(1)
    server.esmtp_features['auth'] = 'LOGIN DIGEST-MD5 PLAIN'
    server.login(self.username, self.password)
    server.sendmail(self.sender, email, message.as_string())
  
  def sendAccountVerificationOtp(self, email: str, otp: str) -> bool:
    html : str = f"""
      <html>
        <body>
          <p>Please use this otp: {otp} to verify you account!</p>
        </body>
      </html>
    """

    self.bgTask.add_task(self.sendMail, email, html, "Account verification otp!")
    return True
  
  def sendForgotPasswordOtp(self, email: str, otp: str) -> bool:
    html : str = f"""
      <html>
        <body>
          <p>Please use this otp: {otp} to reset you password!</p>
        </body>
      </html>
    """

    self.bgTask.add_task(self.sendMail, email, html, "Password reset otp!")
    return True