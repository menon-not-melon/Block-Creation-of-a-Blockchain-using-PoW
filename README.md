# Simple Block Creation with Proof of Work (PoW) 
A simple implementation on the creation of a Block of a Blockchain based Currency.

## Introduction
Welcome to the Simple Block Creation with Proof of Work (PoW) implementation in Python! This project demonstrates the creation of a basic blockchain system, where users can input a number of transactions to be added to a block. Each transaction includes the sender, receiver, and amount. The system then uses a brute force method to find a hash that meets the predefined difficulty level for mining the block.

The Proof of Work concept is widely used in blockchain technology to ensure the security and immutability of the blockchain. It requires miners to perform computational work to find a hash value that satisfies specific criteria, making it difficult and resource-intensive for attackers to tamper with the blockchain.

## Features
* Block creation: Users can input a number of transactions to be added to a block.
* Transaction details: Each transaction includes sender, receiver, and amount.
* Proof of Work: The system automatically computes the hash that fits the predefined difficulty level using brute force.

## How to Use
* Clone the repository to your local machine:
```python
git clone https://github.com/menon-not-melon/Block-Creation-of-a-Blockchain-using-PoW.git
```
* Run the python script.
* Follow the on-screen instructions:
  * Input the number of transactions to be added to the block.
  * For each transaction, enter the sender, receiver, and amount.
* The system will then automatically start the mining process and brute force the hash to meet the predefined difficulty level.
* Once the mining process is complete, the block with the valid hash will be added to the blockchain.

## Customization
You can customize the difficulty level for mining the block by modifying the self.difficulty variable in the blockchain.py script at line 30.
```python
        self.pending_transactions = []
        self.difficulty = 5
```
It has been predefined as 5. A higher difficulty level will require more computation and time to find a valid hash.

## Acknowledgments
We would like to thank the blockchain community for its valuable contributions and open-source projects that inspire us.
