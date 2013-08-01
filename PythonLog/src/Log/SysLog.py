'''
Created on 08/07/2013

@author: karedel
'''

import logging.handlers
from Constants import Constants

class SysLog():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def __setLogger(self, levelParam, message):
        """write in syslog
        
        Keyword arguments:
        levelParam -- 1-DEBUG. 2-INFO. 3-WARNING. 4-CRITICAL
        message -- Exception.message
        
        """
        
        my_logger = logging.getLogger(Constants.pythonLog)
        
        if levelParam==1:
            my_logger.setLevel(logging.DEBUG)
        elif levelParam==2:
            my_logger.setLevel(logging.INFO)
        elif levelParam==3:
            my_logger.setLevel(logging.WARNING)
        elif levelParam==4 :
            my_logger.setLevel(logging.CRITICAL)
        else :
            return
            
        handler = logging.handlers.SysLogHandler(address = '/dev/log')
        
        formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
        handler.setFormatter(formatter)

        my_logger.addHandler(handler)

        my_logger.debug(message)
    
    def writeLogDebug(self, message):
        self.__setLogger(1, message)
        
    def writeLogInfo(self, message):
        self.__setLogger(2, message)
        
    def writeLogWarning(self, message):
        self.__setLogger(3, message)
        
    def writeLogCritical(self, message):
        self.__setLogger(4, message)
            