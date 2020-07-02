"""
Class for listening to 

@author: Joseph Reid
"""
import socket
import os

class ReportReceiver:
    
    def __init__(self, headerSize, port, filename = "programs.log", filepath = './', hostname = socket.gethostname()):
        self.port = port
        self.hostname = hostname
        self.headerSize = headerSize
        self.filename = filename
        self.filepath = filepath
        
    #Check existence of log file and then write to it
    def commitToFile(self, message):
        location = self.filepath + self.filename
        if not os.path.exists(location):
            file = open(location, "w")
        else:
            file = open(location, "a")
        file.write(message)
        file.close()
        
    #Main routine. Listens for incoming connections, and ends when connection
    # is severed from the other end
    def listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        try:
            self.socket.listen()
            connection, address = self.socket.accept()
            fullMessage = ''
            newMessage = True
            while True:
                #Chunk the message into 128 byte segments to not take up too
                #much memory with the buffer
                message = connection.recv(128)
                if newMessage:
                    try:
                        messageLength = int(message[:self.headerSize])
                        newMessage = False
                    except:
                        print("empty message received, assume connection closed")
                        break
                fullMessage += message.decode("utf-8")
                if len(fullMessage)-self.headerSize == messageLength:
                    self.commitToFile(fullMessage[self.headerSize:])
                    fullMessage = ''
                    newMessage = True
            return None
        except KeyboardInterrupt:
            print("ending")
        
