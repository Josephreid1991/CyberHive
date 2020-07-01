# -*- coding: utf-8 -*-
"""
Unit tests for the client object

@author: Joseph Reid
"""


import unittest
import socket
from client import ClientReport

class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.localhost = '127.0.0.1'
        self.port = 55556
        self.testReporter = ClientReport(self.localhost, self.port)
        self.testSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.testSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.testSocket.bind((self.localhost, self.port))
    
    def tearDown(self):
        self.testSocket.close()
        
    def testProcessListGeneration(self):
        self.assertIsNotNone(self.testReporter.generateReport(), "Nothing is generated")
        
    def testProcessListReadable(self):
        self.assertTrue(type(self.testReporter.generateReport()) == str, "The generated report is not a string")

    def testConnectionCapability(self):
        self.testSocket.settimeout(1)
        self.testSocket.listen()
        self.testReporter.sendReport()
        while True:
            clientsocket, address = self.testSocket.accept()
            self.assertTrue(1,1)
            break
        
    def testMessageContainsInfo(self):
        self.testSocket.settimeout(1)
        self.testSocket.listen()
        self.testReporter.sendReport()
        while True:
            clientsocket, address = self.testSocket.accept()
            data = clientsocket.recv(1000000)
            data = data.decode("utf-8")
            self.assertIn('pid', data)
            self.assertIn('Name', data)
            break
    
if __name__ == '__main__':
    unittest.main()