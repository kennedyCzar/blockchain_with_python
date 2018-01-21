'''
blockchain file for python
'''

import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from textwrap import dedent


#create a class first
class Blockchain(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.chain = []
		self.current_transactions = []
		#super(ClassName, self).__init__()
		#self.arg = arg
		

	def proof_of_work(self, last_proof):
		'''
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        '''
		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof

	@staticmethod
	def valid_proof():
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.SHA-256(guess).hexdigest()
		return guess_hash[:4] == "0000"
		'''
	Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
    	'''
        

	def new_block(self):
		block = {
		'index': len(self.chain) + 1,
		'timestamp': time(),
		'transactions': self.current_transactions,
		'proof': proof,
		'previous_hash': previous_hash or self.hash(self.chain[:-1]),
		}
		"""
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        

        #Reset current list  of transaction
		self.current_transactions = []

		self.chain.append(block)
		return block


	def new_transaction(self, sender, recipient, amount):
		self.current_transactions.append({
        	'sender': sender,
        	'recipient': recipient,
        	'amount': amount,
        	})
		return self.last_block['index'] + 1

	@property
	def last_block(self):
        	return self.chain[:-1]

	@staticmethod
	def hash(block):
		block_string = json.dumps(block, sort_keys = True).encode()
		return hashlib.SHA-256(block_string).hexdigest()


#Instantiate our Node
app = Flask(__name__)

#Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

#instatiate the blockchain
blockchain = Blockchain()

@app.route('/mine', methods = ['GET'])
def mine():
	#We run the proof of the work algorithm to get the next proof...
	last_block = blockchain.last_block
	last_proof = last_block['proof']
	proof = blockchain.proof_of_work(last_proof)

	blockchain.new_transaction(
		sender = "0",
		recipient = node_identifier,
		amount = 1
		)
	#forge the new Block by adding it to the chain
	previous_hash = blockchain.hash(last_block)
	block = blockchain.new_block(proof, previous_hash)

	#response
	response = {
	'message': "NewBlock Forged",
	'index': block['index'],
	'transactions': block['transactions'],
	'proof': block['proof'],
	'previous_hash': block['previous_hash'],
	}
	#return "we'll mine a new Block"
	return jsonify(response), 200

@app.route('/transactions/new', methods = ['POST'])
def new_transaction():
	values = request.get_json()

	#Check tha the required fields are in the POST'ed data
	required = ['sender', 'recipient', 'amount']
	if not all(k in values for k in required):
		return 'Missing values', 400

	#Create a new Transaction
	index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

	response = {'message': f'Transaction will be added to Block to Block {index}'}
	return jsonify(response), 201
	#return "we'll add a new transaction"

@app.route('/chain', methods = ['GET'])
def full_chain():
	response = {
	'chain': blockchain.chain,
	'length': len(blockchain.chain),
	}
	return jsonify(response), 200

if __name__ ==  '__main__':
	app.run('localhost', port =80)