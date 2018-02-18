from sys import getsizeof
from Block import Block


block1 = Block("Fred sends 5 to Holly")
print("Block 1 Trans: " + block1.getTransactions())
print("Block 1 Hash: " + block1.getCurrentHash())
print()

block2 = Block("Holly send 10 to Rachel", block1)
print("Block 2 Trans: " + block2.getTransactions())
print("Block 2 Hash: " + block2.getCurrentHash())
print()

block3 = Block("Rachel sends 15 to Brian",block2)
print("Block 3 Trans: " + block3.getTransactions())
print("Block 2 Hash: " + block3.getCurrentHash())
print()


print()
print("Changing Block 1 Transactions")
block1.setTransactions("Samy sends 200 to Holly")
print("Block 1 Trans: " + block1.getTransactions())
print("Block 1 Hash: " + block1.getCurrentHash())
print()

print("Block 2 Trans: " + block2.getTransactions())
print("Block 2 Hash: " + block2.getCurrentHash())
print()

print("Block 3 Trans: " + block3.getTransactions())
print("Block 2 Hash: " + block3.getCurrentHash())
print()
