'''
Created on 08/07/2013

@author: karedel
'''
# -*- encoding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from Constants import Constants

class EmailLog():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def sendEmail(self, message):
        #message creation
        msg = MIMEText(message)
        
        #server connection
        msg['Subject'] = Constants.emailSubject 
        msg['From'] = Constants.emailFrom 
        msg['To'] = Constants.emailTo
        
        # Auth 
        mailServer = smtplib.SMTP(Constants.emailServer,Constants.emailPort) 
        mailServer.ehlo() 
        mailServer.starttls() 
        mailServer.ehlo() 
        mailServer.login(Constants.emailFrom, Constants.emailPass)

        # Send
        mailServer.sendmail(Constants.emailFrom, Constants.emailTo, msg.as_string())   
        
        # close connection
        mailServer.close()
        
        
        
        