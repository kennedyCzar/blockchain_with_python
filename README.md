# blockchain_with_python
 >Step 1: Building a Blockchain Open up your favourite text editor or IDE, personally I ❤️ Sublime text. 
Create a new file, called blockchain.py. We’ll only use a single file, but if you get lost, 
you can always refer to the source code.  
Representing a Blockchain We’ll create a Blockchain class whose constructor creates an initial 
empty list (to store our blockchain), and another to store transactions. Here’s the blueprint for our class:

Our Blockchain class is responsible for managing the chain. 
It will store transactions and have some helper methods for 
adding new blocks to the chain. Let’s start fleshing out some methods.

What does a Block look like?
Each Block has an index, a timestamp (in Unix time), 
a list of transactions, a proof (more on that later),
and the hash of the previous Block.

Here’s an example of what a single Block looks like:

'''
-block = {
 -   'index': 1,
  -  'timestamp': 1506057125.900785,
   - 'transactions': [
     -   {
           - 'sender': "8527147fe1f5426f9dd545de4b27ee00",
          -  'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
          -  'amount': 5,
      -  }
  -  ],
    
'''
At this point, the idea of a chain should be apparent—each new block contains within itself, 
the hash of the previous Block. This is crucial because it’s what gives blockchains immutability: 
If an attacker corrupted an earlier Block in the chain then all subsequent blocks will contain incorrect hashes.

Does this make sense? If it doesn’t, take some time to let it sink in—it’s the core idea behind blockchains.
