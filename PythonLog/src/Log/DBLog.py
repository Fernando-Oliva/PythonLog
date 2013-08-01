'''
Created on 15/07/2013

@author: karedel
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import os.path

class DBLog():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def __writeDB(self, con, message):
        with con:
                cur = con.cursor()    
                cur.execute("INSERT INTO Log VALUES(NULL,'" + message + "')")
                cur.execute("commit")
                
        con.close()
        
    def __createTable(self, message):
        con = lite.connect('test.db') 
        con.execute("CREATE TABLE Log(id integer primary key not null autoincrement, Error TEXT)")
        
        self.__writeDB(con, message)
        
        con.close()
            
    def writeDBLog(self, message):
        if not os.path.exists('test.db'):
            self.__createTable(message)
        else :
            con = lite.connect('test.db')
            
            self.writeDBLog(con, message)