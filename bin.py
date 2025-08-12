from sm4 import *
import random
import numpy as np
import pickle
from sklearn.utils import shuffle


class Experiment():
    def stringtoasciidecimal(text, length):
        decimal = 0
        for i in text:
            decimal <<= 8
            decimal += ord(i)
            # print(hex(decimal))
        if length < 16:
            decimal <<= 8 * (16 - length)
        return decimal


    def __init__(self):
        print("Enter which round you want to capture [1-32]:")
        num_round = int(input())
        if num_round < 1 or num_round > 32:
            print("Invalid round...")
            return -1

        plaintexts = list(pickle.load(open('plaintexts.pkl', "rb")))
        # number of samples
        num_samples = len(plaintexts)
        #num_samples_2x = num_samples * 2
        max_limit_128bit = 2 ** 128
        with open('ciphertexts.bin', 'wb') as file:
            for i in range(0,100):

                # key value (Defaults: Random 128bits)
                key = random.randint(0, max_limit_128bit)
                for num_sample in range(0, num_samples):
                    print(num_sample)
                    plaintext = plaintexts[num_sample]
                    len_pt = len(plaintext)
                    if len_pt < 17:
                        plaintext = Experiment.stringtoasciidecimal(plaintext, len_pt)
                    else:
                        plaintext = Experiment.stringtoasciidecimal(plaintext[0:16], 16)
                    # Ciphertexts are generated at particular round of SM4 encryption
                    ciphertext, _ = encrypt(plaintext, key, num_round)
                    file.write(ciphertext.to_bytes(16,'big'))

if __name__ == '__main__':
    Experiment()
