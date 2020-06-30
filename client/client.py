# -*- coding: utf-8 -*-
"""
Class for generating a list of running processes on a client machine 
and sending a report to a given server

@author: Joseph Reid
"""


import psutil

class ClientReport:
    def __init__(self):
        pass
    
    def generateReport(self):
        #get running processes on the system
        runningProcesses = psutil.process_iter(['pid', 'name'])
        
        #Make the report into a string
        reportString = ''
        for item in runningProcesses:
            reportString += "pid: "+ str(item.pid) + " Name: " + item.name() + "\n"
        
        return reportString
    
    