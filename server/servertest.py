# -*- coding: utf-8 -*-
"""
Class for testing the server side of the application

@author: josep
"""

import unittest
import socket
import os
import threading
from time import sleep
from server import ReportReceiver

class TestServer(unittest.TestCase):
    
    def setUp(self):
        self.localhost = '127.0.0.1'
        self.port = 55555
        self.filepath = "./"
        self.filename = "test.log"
        self.headerSize = 10
        self.testListener = ReportReceiver(self.headerSize, self.port, self.filename, self.filepath, self.localhost,)
        self.testSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self):
        self.testSocket.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
        
    def testConnection(self):
        self.listeningThread = threading.Thread(target=self.testListener.listen, args = ())
        self.listeningThread.deamon = True
        self.listeningThread.start()
        self.testSocket.connect((self.localhost, self.port))
        testMessage = "This is a test message"
        testMessage = f"{len(testMessage):<{self.headerSize}}" + testMessage
        self.testSocket.send(bytes(testMessage, "utf-8"))
        sleep(0.01)
        self.assertTrue(os.path.exists(self.filename))
        
    
if __name__ == '__main__':
    unittest.main()