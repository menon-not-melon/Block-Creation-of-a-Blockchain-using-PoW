import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True, default=str)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"\nBlock mined (Nonce Value): {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [Block(0, None, [])]
        self.pending_transactions = []
        self.difficulty = 5

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine(self, miner_address):
        if not self.pending_transactions:
            return False

        last_block = self.chain[-1]
        new_block = Block(last_block.index + 1, last_block.hash, self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = [Transaction(None, miner_address, 1)]

        return new_block

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender == address:
                    balance -= transaction.amount
                elif transaction.receiver == address:
                    balance += transaction.amount

        return balance


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount


# Example usage
if __name__ == '__main__':
    blockchain = Blockchain()

    # Add transactions
    num = int(input("\nEnter number of transactions to be added : "))
    nodes = set()
    for i in range(0, num):
        sender = input("Enter Sender : ")
        reciever = input("Enter Reciever : ")
        amount = int(input("Enter Payment Amount : "))
        blockchain.add_transaction(Transaction(sender, reciever, amount))
        nodes.add(sender)
        nodes.add(reciever)

    # Mine new block
    miner_address = 'Miner'
    mined_block = blockchain.mine(miner_address)

    # Check balance
    for i in nodes:
        balance = blockchain.get_balance(i)
        print(f"{i}'s balance: {balance}")

    miner_balance = blockchain.get_balance(miner_address)
    print(f"Miner's balance: {miner_balance}")