'''
Created on 08/07/2013

@author: karedel
'''

from datetime import datetime
from Constants import Constants
import os.path

class FileLog():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
            
    def __creartxt(self):
        logFile = open(Constants.logFile, mode='w')
        logFile.close()
    
    def __log(self, message):
        d = datetime.today()
        
        logFile = open(Constants.logFile, mode='a')
        logFile.write(str(d) + '\n')
        logFile.write(message + '\n')
        logFile.write('----------------- \n')
        logFile.close()
        
    def writeFile(self, message):
        if os.path.exists(Constants.logFile):
            self.__log(message)
        else:
            self.__creartxt()
            self.__log(message)