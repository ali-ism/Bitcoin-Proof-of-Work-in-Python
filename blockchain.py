from hashlib import sha256
from time import time
import numpy as np
from binascii import hexlify
from typing import NamedTuple, Tuple


class BlockData(NamedTuple):
    aub_id : str
    email: str
    full_name: str


class Block():
    def __init__(self, prev_hash: str, data: BlockData) -> None:
        self.prev_hash = prev_hash

        self.data = data
        self.aub_id_hex = hexlify(self.data.aub_id.encode())
        self.email_hex = hexlify(self.data.email.encode())
        self.full_name_hex = hexlify(self.data.full_name.encode())

        self.timestamp = np.uint32(time())

        self.nonce = np.uint32(0x00000000)
        self.overflowed = False
    
    def hash(self) -> str:
        hash_fct = sha256()
        hash_fct.update(self.prev_hash.encode())
        hash_fct.update(self.timestamp)
        hash_fct.update(self.aub_id_hex)
        hash_fct.update(self.email_hex)
        hash_fct.update(self.full_name_hex)
        hash_fct.update(self.nonce)
        if self.overflowed:
            hash_fct.update(self.overflow_helper)
        return hash_fct.hexdigest()

    def mine(self, difficulty: int) -> Tuple[float,int]:
        target = (256 - difficulty) * '1'
        target = target.zfill(256)
        target = int(target, 2)
        counter = 0
        self.nonce = np.uint32(0x00000000)
        self.overflowed = False
        self.overflow_helper = b''
        start_time = time()
        while int(self.hash(),16) > target:
            try:
                self.nonce += 1
            except OverflowError:
                self.overflowed = True
                self.nonce = np.uint32(0x00000000)
                self.overflow_helper += b'0'
                continue
            counter += 1
            #print(f'Iterations: {counter}', end='\r')
        elapsed_time = time() - start_time
        #print(f'Elapsed time: {elapsed_time} seconds')
        return elapsed_time, counter
    
    def display(self) -> None:
        print('---------------Header---------------')
        print(f'Previous Hash: {self.prev_hash}')
        print(f'Timestamp: {self.timestamp}')
        print(f'nonce: {self.nonce}')
        print('---------------Data---------------')
        print(f'Full Name: {self.data.full_name}')
        print(f'Email: {self.data.email}')
        print(f'AUB ID: {self.data.aub_id}')
        if self.overflowed:
            print(f'Overflow Helper: {self.overflow_helper.decode()}')
    
    def display_hex(self) -> None:
        print('---------------Header---------------')
        print(self.prev_hash)
        print(hex(self.timestamp)[2:])
        print(hex(self.nonce)[2:])
        print('---------------Data---------------')
        print(self.full_name_hex.decode())
        print(self.email_hex.decode())
        print(self.aub_id_hex.decode())
        if self.overflowed:
            print(self.overflow_helper.decode())


class Blockchain():
    def __init__(self) -> None:
        self.blocks = []
    
    def add(self, new_block: Block):
        if new_block.prev_hash == self.blocks[-1].hash():
            self.blocks.append(new_block)
        else:
            print('The new block must point to the last block in the chain.')
    
    def __getitem__(self, index):
        return self.blocks[index]
    
    def __len__(self):
        return len(self.blocks)