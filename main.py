
from sm4 import *
import random
import numpy as np
import pickle
from sklearn.utils import shuffle

class Experiment():
    def stringtoasciidecimal(text,length):
            decimal = 0
            for i in text:
                decimal<<=8
                decimal+=ord(i)
                #print(hex(decimal))
            if length<16:
                decimal<<=8*(16-length)
            return decimal
    # Rotate bits of number
    # Function to left
    # rotate n by d bits
    def leftRotate(n, d, INT_BITS):
        # In n<<d, last d bits are 0.
        # To put first 3 bits of n at
        # last, do bitwise or of n<<d
        # with n >>(INT_BITS - d)
        return (n << d)|(n >> (INT_BITS - d))

    # Function to right
    # rotate n by d bits
    def rightRotate(n, d, INT_BITS):
        # In n>>d, first d bits are 0.
        # To put last 3 bits of at
        # first, do bitwise or of n>>d
        # with n <<(INT_BITS - d)
        return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF

    def __init__(self):
        print("Enter which round you want to capture [1-32]:")
        num_round = int(input())
        if num_round<1 or num_round>32:
            print("Invalid round...")
            return -1

        plaintexts = list(pickle.load(open('plaintexts.pkl', "rb")))
        # number of samples
        num_samples = len(plaintexts)
        num_samples_2x = num_samples *2
        max_limit_128bit = 2**128

        # key value (Defaults: Random 128bits)
        key = random.randint(0, max_limit_128bit)
        
        data = np.zeros((num_samples_2x,32), dtype=np.uint8)
        label = np.zeros((num_samples_2x), dtype=np.uint8)

        for num_sample in range(0,num_samples):
            print(num_sample)
            label[num_sample] = 1
            plaintext = plaintexts[num_sample]
            len_pt = len(plaintext)
            if len_pt<17:
                plaintext = Experiment.stringtoasciidecimal(plaintext,len_pt)
            else:
                plaintext = Experiment.stringtoasciidecimal(plaintext[0:16],16)
            # Ciphertexts are generated at particular round of SM4 encryption
            ciphertext, _ = encrypt(plaintext, key, num_round)
            ciphertext1 = ciphertext ^ Experiment.rightRotate(ciphertext, 1, 128)
            ciphertext2 = ciphertext ^ Experiment.rightRotate(ciphertext, 2, 128)
            a = ciphertext1
            b = ciphertext2
            for i in range(0,16):
                data[num_sample][31-i] = a&255
                data[num_sample][15-i] = b&255
                a = a>>8
                b = b>>8
        for num_sample in range(num_samples,num_samples_2x):
            print(num_sample)
            label[num_sample] = 0
            plaintext = random.randint(0, max_limit_128bit)
            # Ciphertexts are generated at particular round of SM4 encryption
            ciphertext = plaintext
            #ciphertext, _ = encrypt(plaintext, key, num_round)
            ciphertext1 = ciphertext ^ Experiment.rightRotate(ciphertext, 1, 128)
            ciphertext2 = ciphertext ^ Experiment.rightRotate(ciphertext, 2, 128)
            a = ciphertext1
            b = ciphertext2
            for i in range(0,16):
                data[num_sample][31-i] = a&255
                data[num_sample][15-i] = b&255
                a = a>>8
                b = b>>8
        data, label = shuffle(data, label)
        data = np.unpackbits(data, axis=1)
        np.save("data.npy",data)
        np.save("label.npy",label)
if __name__ == '__main__':
    Experiment()
