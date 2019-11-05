import datetime
import hashlib


class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previouts_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def __hash__(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previouts_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.__hash__()) + "\nBlockNo: " + str(self.blockNo) + "\n nonce: " + str(
            self.nonce) + "\ndata: " + str(self.data) + "\npreviouts_hash: " + str(
            self.previouts_hash) + "\ntimestamp: " + str(self.timestamp)


class Blockchain:
    maxNonce = 2 ** 32
    diff = 10
    target = 2 ** (256 - diff)

    block = Block("Genesis")
    head = block

    def add(self, block):
        block.previouts_hash = self.block.__hash__()
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.__hash__(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


blockchain = Blockchain()
for n in range(10):
    blockchain.mine(Block("Block " + str(n + 1)))
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
