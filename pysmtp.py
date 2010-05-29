#!/usr/bin/env python

"""
pysmtp: an easy way to send email from the command line on Mac OS X

Revision History:
0.1.0 - 2010-05-10 - initial release

Copyright 2010 Luke D Hagan
Software License: Do whatever you want.
Disclaimer: This software is provided 'AS IS' -- use at your own risk.

"""

from keychain import keychain
import mail

default_subject = "Message from pysmtp"
default_text = "This email was sent by pysmtp"
default_port = 587
default_keychain = 'login'

def getPassword(key, username, server):
    k=keychain.Keychain()
    keychaindata = k.get_internet_password(key, username, server)
    return keychaindata['password']

def main():
    from optparse import OptionParser
    parser = OptionParser(usage="%prog <from address> <to address> [options]")
    parser.add_option(  "-l", "--subject", action="store", type="string", default=default_subject, dest="subject", help="message subject text")
    parser.add_option(  "-c", "--text", action="store", type="string", default=default_text, dest="text", help="message body text")
    
    parser.add_option(  "-a", "--attach", action="store", type="string", default=False, dest="attach", help="file to attach")
    parser.add_option(  "-s", "--server", action="store", type="string", default=False, dest="server", help="SMTP server address")
    parser.add_option(  "-p", "--port", action="store", type="int", default=default_port, dest="port", help="SMTP server port number")
    parser.add_option(  "-k", "--keychain", action="store", type="string", default=default_keychain, dest="key", help="name of keychain")
    
    def send():
        mail.mail(username, password, to, options.subject, options.text, options.port, options.attach, options.server)
    
    (options, args) = parser.parse_args()
    arg_length = len(args)
    
    if arg_length == 0:     
        print("Error: sender/recipient address not specified")
        
    if arg_length == 1 or arg_length == 2:
        username = args[0]
        password = getPassword(options.key, username, options.server)
        
    if arg_length == 1:
        to = args[0]
        send()
        
    if arg_length == 2:
        to = args[1]
        send()
        
    if arg_length > 2:
        print("Error: too many arguments (2 max)")
    
if __name__ == "__main__":
    main()