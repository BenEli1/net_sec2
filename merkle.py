#Ben Eli, 319086435, Daniel Bronfman, 315901173
# -*- coding: utf-8 -*-
import hashlib
import math
import base64

def sha256_from_str(string):
    return (hashlib.sha256((string.encode("utf-8")))).hexdigest()




class Node:

    def __init__(self,data=None,left=None,right=None):
        self._left = left
        self._right = right
        self._data = data

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,value):
        self._data = value

    @left.setter
    def left(self,value):
        self._left = value

    @right.setter
    def right(self,value):
        self._right = value


class MerkleTree:

    def __init__(self):
        self._leaf_id = 0
        self._root = Node(None)
        self._values = []



    def recursive_build(self,values):
        temp = []
        if len(values) <= 1:
            return values[0]
        while len(values) >= 1:
            if len(values) == 1:
                temp.append(Node(data = values[0].data,left = values[0]))
                values = values[1:]
            else:
                temp.append(Node(data = sha256_from_str(values[0].data+values[1].data),left = values[0],right = values[1]))
                values = values[2:]
        return self.recursive_build(temp)

    def generate_tree(self):
        self._root = self.recursive_build(self._values)

    # on input of 1
    def add_leaf(self,leaf_data: str):
        """
       input : string until newline
       output :
       """
        self._values.append(Node(data = sha256_from_str(leaf_data)))
        self.generate_tree()

    # on input of 2
    def calc_root(self):
        """
        input :
        output : root value in hex
        """
        if self._root.data is None:
            print("")
            return
        self.generate_tree()
        print(self._root.data)

    # on input of 3
    def generate_incl_proof(self,leaf_id):
        """
        input : X the number of the leaf - leftmost is 0
        output : root{space}hashX{space}...{space}hashY
        """
        pass

    # on input of 4
    def check_incl_proof(self,leaf_val):
        """
       input : string, the information represented by the leaf
       output : True if the proof is correct False otherwise
       """
        pass

    #on input of 5
    def generate_rsa_pair(self):
        """
        input:
        output: private key and public key
        """

    #on input of 6
    def generate_signature(self,sig_key):
        """
        input: signature key
        output: signature created by passed key
        """

    #on input of 7
    def verify_signature(self,ver_key,sig,to_ver):
        """
        input: verification key,signature,text to verify
        output: True if signature is correct, False otherwise
        """

def main(tree):

    user_choice = None
    user_input = None
    #TODO: finish switch case
    user_choice = input()
    user_choice = int(user_choice)
    match user_choice:
        case 0:
            exit()
        case 1:
            user_input = input()
            tree.add_leaf(leaf_data = user_input)
        case 2:
            tree.calc_root()
        case 3:
            user_input = input()
            tree.generate_incl_proof(leaf_id = user_input)
        case 4:
            user_input = input()
            tree.check_incl_proof(leaf_val = user_input)
        case 5:
            tree.generate_rsa_pair()
        case 6:
            user_input = input()
            tree.generate_signature(sig_key = user_input)
        case 7:
            user_input1 = input()
            user_input2 = input()
            user_input3 = input()
            tree.verify_signature(ver_key = user_input1,sig = user_input2,to_ver = user_input3)
        case _:
            return

if __name__ == '__main__':
    try:
        tree = MerkleTree()
        while True:
            main(tree)
    except KeyboardInterrupt as e:
        print(e)
