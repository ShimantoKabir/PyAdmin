import smtplib
from abc import ABC, abstractmethod

class EmailService(ABC):
  
  @abstractmethod
  def setAccountVerification(email: str, otp: str) -> bool:
    pass