PythonLog
=========

Log for Python


Basic log for Python with the following features:

Write error in file
Write error in syslog
Send email with error
Write error in database

This log is organized by level of error and each of these functions makes some or other functions:

DEBUG
    FileLog
    SysLog -- Configurable

INFO
    FileLog
    SysLog -- Configurable
    DBLog -- Configurable

WARNING
    FileLog
    SysLog -- Configurable
    EmailLog -- Configurable
    DBLog -- Configurable

CRITICAL
    FileLog
    SysLog
    EmailLog
    DBLog

