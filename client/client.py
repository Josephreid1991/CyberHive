# -*- coding: utf-8 -*-
"""
Class for generating a list of running processes on a client machine 
and sending a report to a given server

@author: Joseph Reid
"""


import psutil
import socket
import time
import threading

class ClientReport:
    def __init__(self, ipAddress, port):
        self.address = ipAddress
        self.port = port
        self.headerSize = 10
        
    
    #Function to create socket and establish connection
    def createSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.socket.connect((self.address,self.port))
        except:
            print("connection impossible. Assume no listening port")
    
    def generateReport(self):
        #get running processes on the system
        runningProcesses = psutil.process_iter(['pid', 'name'])
        
        #Make the report into a string
        reportString = 'Report '
        reportString += str(time.ctime(time.time())) + '\n'
        for item in runningProcesses:
            reportString += "pid: "+ str(item.pid) + " Name: " + item.name() + "\n"
        
        return reportString
    
    def sendReport(self):
        #generate report string
        report = self.generateReport()
        #attach header
        report = f"{len(report):<{self.headerSize}}" + report
        if not hasattr(self, 'socket'):
            self.createSocket()
        #send report
        self.socket.send(bytes(report, "utf-8"))
        return None
        
    def report(self):
        #start a timer to execute the next report in 5 seconds
        self.thread = threading.Timer(5, self.report)
        self.thread.start()
        #send report now
        self.sendReport()
        #return to kill threading
        return None
        
    #tear down functionality
    def close(self):
        if hasattr(self, "thread"):
            self.thread.cancel()
        if hasattr(self, 'socket'):
            self.socket.close()
        
    