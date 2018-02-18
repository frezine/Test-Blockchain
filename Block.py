from hashlib import sha3_256 as sha256
from sys import getsizeof

class Block():


    def __init__(self, transactions, prevBlock = None):

        self.transactions = transactions
        self.prevBlock = prevBlock


    def getTransactions(self):
        """Get Transaction String"""
        return self.transactions


    def setTransactions(self, transactions):
        """Set Transaction String"""
        self.transactions = transactions

    def getRawString(self):
        """Return 'hash(previousBlock)':'transactions'"""
        if self.prevBlock == None:
            return "{0}:{1}".format("Genesis",self.transactions).encode('utf-8')
        else:
            return "{0}:{1}".format(self.prevBlock.getCurrentHash(),self.transactions).encode('utf-8')

    
    def getCurrentHash(self):
        """Return sha256 hash of 'hash(previousBlock)':'transactions'"""
        if self.prevBlock == None:
            return sha256(self.getRawString()).hexdigest()
        else:
            return sha256("{0}:{1}".format(self.getRawString()).hexdigest()


    def getPreviousRawString(self):
        """Get Previous Raw String"""
        if self.prevBlock == None:
            return None
        else:
            return self.prevBlock.getRawString()

    def getPreviousHash(self):
        """Get Previous Hash"""
        if self.prevBlock == None:
            return None
        else:
            return self.prevBlock.getCurrentHash()









