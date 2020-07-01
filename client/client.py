# -*- coding: utf-8 -*-
"""
Class for generating a list of running processes on a client machine 
and sending a report to a given server

@author: Joseph Reid
"""


import psutil
import socket

class ClientReport:
    def __init__(self, ipAddress, port):
        self.address = ipAddress
        self.port = port
    
    def generateReport(self):
        #get running processes on the system
        runningProcesses = psutil.process_iter(['pid', 'name'])
        
        #Make the report into a string
        reportString = ''
        for item in runningProcesses:
            reportString += "pid: "+ str(item.pid) + " Name: " + item.name() + "\n"
        
        return reportString
    
    def sendReport(self):
        report = self.generateReport()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.address,self.port))
        self.socket.send(bytes(report, "utf-8"))
        self.socket.close()
        
        
    