import sys
from FileLog import FileLog
from SysLog import SysLog
from EmailLog import EmailLog
from Constants import Constants
from DBLog import DBLog

class Log:
    
    fLog = FileLog()
    sLog = SysLog()
    eLog = EmailLog()
    dLog = DBLog()

    def errorDebug(self, message, configSysLog=1):
        """error level Debug.
        
        Keyword arguments:
        message -- Exception.message
        configSysLog -- value for activate write in syslog (default 1)
        
        """
        self.fLog.writeFile(message)
        
        if configSysLog == 1:
            self.sLog.writeLogDebug(message) #Config
        
    def errorInfo(self, message, configSysLog=1, configDBLog=1): #message = Exception.message
        """error level Info.
        
        Keyword arguments:
        message -- Exception.message
        configSysLog -- value for activate write in syslog (default 1)
        configDBLog -- value for activate write in database (default 1)
        
        """
        self.fLog.writeFile(message)
        
        if configSysLog == 1:
            self.sLog.writeLogInfo(message) #Config
        
        if configDBLog == 1:
            self.dLog.writeDBLog(message) #Config
            
    def errorWarning(self, message, configSysLog=1, configEmailLog=1, configDBLog=1):
        """error level Warning.
        
        Keyword arguments:
        message -- Exception.message
        configSysLog -- value for activate write in syslog (default 1)
        configEmailLog -- value for activate send email (default 1)
        configDBLog -- value for activate write in database (default 1)
        
        """
        self.fLog.writeFile(message)
        
        if configSysLog == 1:
            self.sLog.writeLogWarning(message) #Config
            
        if configEmailLog == 1:
            self.eLog.sendEmail(message) #Config
            
        if configDBLog == 1:
            self.dLog.writeDBLog(message) #Config
            
    def errorCritical(self, message):
        """error level Critical.
        
        Keyword arguments:
        message -- Exception.message
        
        """
        self.fLog.writeFile(message)
        self.sLog.writeLogCritical(message)
        self.eLog.sendEmail(message)
        self.dLog.writeDBLog(message)
    