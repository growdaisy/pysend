class Contact:
   def __init__(self, name, email):
      self.name = name
      self.email = email

class Server:
   def __init__(self):
      pass

   def connect(self):
      pass

   def send(self, email):
      raise NotImplementedError

class Email:
   def __init__(self, sender, receivers, subject, body,
                cc=[], bcc=[]):
      self.sender = sender
      self.receivers = receivers
      self.cc = cc
      self.bcc = bcc
      self.subject = subject
      self.body = body
