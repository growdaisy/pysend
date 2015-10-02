import requests
from .classes import Contact, Email
from . import classes

class SendGridWebApiServer(Server):
   def __init__(self, url, apiKey):
      self.url = url
      self.apiKey = apiKey

   def connect(self):
      pass

   # FixMe: [correctness] Support more than one recipient
   # FixMe: [correctness] Support cc and bcc fields
   def send(self, email):
      headers = {
         'Authorization': 'Bearer {}'.format(self.apiKey)
      }

      payload = {
         'from': email.sender.email,
         'fromname': email.sender.name,
         'to': email.receivers[0].email,
         'toname': email.receivers[0].name,
         'subject': email.subject,
         'html': email.body
      }

      requests.post(sendgridUrl, headers=headers, data=payload)
