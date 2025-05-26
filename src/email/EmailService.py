import smtplib
from abc import ABC, abstractmethod

class EmailService(ABC):
  
  @abstractmethod
  def sendAccountVerificationOtp(email: str, otp: str) -> bool:
    pass

  @abstractmethod
  def sendForgotPasswordOtp(email: str, otp: str) -> bool:
    pass