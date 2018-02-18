from hashlib import sha3_256 as sha256
from sys import getsizeof

class Block():

##  Initialize current transactions
##  Initialize Hash Object of previous Block
    def __init__(self, transactions, prevBlock = None):

        self.transactions = transactions
        self.prevBlock = prevBlock
        
##        if self.prevBlock == None:
##            self.unhashedString = "Genesis" + ":" + self.transactions
##            self.unhashedString = self.unhashedString.encode('utf-8')
##        else:
##            self.unhashedString = self.getPreviousHash() + ":" + self.transactions
##            self.unhashedString = self.unhashedString.encode('utf-8')
##
##        self.currentHashedBlock = sha256(self.unhashedString).hexdigest()

        

    def getPreviousHash(self):        
        if self.prevBlock == None:
            return None
        else:
            return self.prevBlock.getCurrentHash()


    def getTransactions(self):
        return self.transactions

    def setTransactions(self,transactions):
        self.transactions = transactions

    
    def setPreviousHash(self):
        if self.prevBlock != None:
            self.prevBlock.currentHashedBlock()

    def getCurrentHash(self):
        if self.prevBlock == None:
            return sha256("{0}:{1}".format("Genesis",self.transactions).encode('utf-8')).hexdigest()
        else:
            return sha256("{0}:{1}".format(self.prevBlock.getCurrentHash(),self.transactions).encode('utf-8')).hexdigest()


    def updateHashBlock(self):
        self.currentHashedBlock = self.currentHashedBlock.update(prevHash + ":" + transactions)



