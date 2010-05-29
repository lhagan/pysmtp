pysmtp
===========
An easy way to send email from the command line on Mac OS X

pysmtp lets you send email from the command line (or another script) with minimal hassle.
It uses the Mac OS X keychain to retrieve your password (no more storing passwords in
plain text!). You can even send attachments. pysmtp has no dependencies (other than Python
and keychain.py, which is included), so there's nothing to compile, install, or configure.


Setup
-------

To get started, you'll need a keychain item that corresponds to the SMTP server you want to
use. Open Keychain Access (in /Applications/Utilities) and go to File > New Password Item...
Set "Keychain Item Name", to your SMTP server; for example "smtp.gmail.com". In the "Account Name"
box, enter your email address, such as "example@gmail.com". Finally, enter your password and
save the item.


Usage
-------

Usage is simple -- there's only one required argument (although you'll probably need more to
do anything useful). The following will send an email to example@gmail.com from example@gmail.com:

    python pysmtp.py example@gmail.com
    
Add a 2nd email address to send to someone other than yourself, and use options to set the
subject, message, file attachment, etc. For a complete list of options, run:

    python pysmtp.py --help

Note that as pysmtp depends on Mac OS X's keychain, it won't work on any other platform.
I'm sure someone else can solve this and I'd be happy to merge in any such enhancements.


License
-------

Copyright 2010 Luke D Hagan

Do whatever you want. Feel free to copy, modify, redistribute, remix, etc. in whatever way you
see fit.


Disclaimer
-------

This software is provided 'AS IS' -- use at your own risk. It works fine for me, but I'm
not to be held responsible for any damage, data loss, security breaches, public
embarrassment, etc. that may result from your use of this software.
