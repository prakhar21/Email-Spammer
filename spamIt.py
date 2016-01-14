'''
    Author: Prakhar Misha
    Date: 29/07/2015
'''

# Importing Packages
import smtplib
import time

# Email Id and account information
to = 'Email Id of other person'
gmail_user = 'Your Email id here'
gmail_pwd = '<Your password here>'

# No. of emails to be sent
mails = 200
for i in range(mails):
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	
	# Subject of the mail
	header = 'To:' + to + '\n' + 'From: '+ gmail_user + '\n' + 'Subject:Hello '+ str(i) +'\n'
	print header
	
	# Email body
	msg = header + '\n LOOOOOL \n\n'
	
	smtpserver.sendmail(gmail_user, to, msg)
	print 'done!'
	smtpserver.close()
	# Time lapse between 2 emails ( 2sec )
	time.sleep(2)
