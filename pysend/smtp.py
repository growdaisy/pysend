import smtplib
from email.mime.text import MIMEText
from email.header import Header
from .classes import Contact, Email
from . import classes

def _outputContact(contact):
   return "{} <{}>".format(contact.name, contact.email)

def _outputEmail(email):
   toOutput = ",".join(_outputContact(c) for c in email.receivers)

   msg = MIMEText(email.body, _charset="UTF-8")
   msg['Subject'] = Header(email.subject, "utf-8")
   msg['From'] = _outputContact(email.sender)
   msg['To'] = toOutput
   if len(email.cc) != 0:
      ccOutput = ",".join(_outputContact(c) for c in email.cc)
      msg['Cc'] = ccOutput
   return msg.as_string()

class SmtpServer(pysend.Server):
   def __init__(self, domain, port, sender, password):
      self.domain = domain
      self.port = port
      self.sender = sender
      self.password = password

   def connect(self):
      self.smtpObj = smtplib.SMTP_SSL(self.domain, self.port)
      self.smtpObj.login(self.sender.email, self.password)

   def send(self, email):
      toAddrs = [c.email for c in email.receivers] + \
                [c.email for c in email.cc] + \
                [c.email for c in email.bcc]
      self.smtpObj.sendmail(self.sender.email, toAddrs,
                            _outputEmail(email))
