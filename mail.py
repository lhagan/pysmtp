#!/usr/bin/env python

"""
SMTP script by Kutuma
http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html
modifications for use in pysmtp by Luke Hagan on 2010-05-10
"""

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

def mail(username, password, to, subject, text, port, attach=None, server=None):
    msg = MIMEMultipart()

    msg['From'] = username
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    if attach:
         part = MIMEBase('application', 'octet-stream')
         part.set_payload(open(attach, 'rb').read())
         Encoders.encode_base64(part)
         part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
         msg.attach(part)
    
    if not server:
        # figure out the server name based on username
        (name, cserver) = username.split('@')
        server = 'smtp.' + cserver

    mailServer = smtplib.SMTP(server, port)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(username, password)
    mailServer.sendmail(username, to, msg.as_string())
    mailServer.quit()