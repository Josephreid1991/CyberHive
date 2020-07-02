# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:15:53 2020

@author: josep
"""

from server import ReportReceiver

ongoingReceiver = ReportReceiver(10, 55555, 'programs.log', '/var/log/', '0.0.0.0')
try:
    ongoingReceiver.listen()
except KeyboardInterrupt:
    print("ending process")