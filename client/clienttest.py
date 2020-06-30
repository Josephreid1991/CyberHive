# -*- coding: utf-8 -*-
"""
Unit tests for the client object

@author: Joseph Reid
"""


import unittest
from client import ClientReport

class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.testReporter = ClientReport()
    
    def testProcessListGeneration(self):
        self.assertIsNotNone(self.testReporter.generateReport(), "Nothing is generated")
        
    def testProcessListReadable(self):
        self.assertTrue(type(self.testReporter.generateReport()) == str, "The generated report is not a string")

    
if __name__ == '__main__':
    unittest.main()