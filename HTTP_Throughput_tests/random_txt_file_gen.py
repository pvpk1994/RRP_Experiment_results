# Random txt file generator of sizes {1KB, 100KB, 1MB} with random letter txt
# Author:: Pavan Kumar Paluri @ RTLAB-UH
# Last Updated May-4, 2020

import numpy as np
import os
# Create multiple txt files of total 1GB
# Creation Method:: Composition => { 1KB : 1000; 100KB : 1000; 1MB: 899 }

num_one_kb_files = 10
num_100_kb_files = 5
num_1_mb_files = 3

# Generate english alphabets
letters = np.array(list(chr(ord('a')+i) for i in range(0, 26)));
# print(letters)

# Form random txt with strings now..
def get_rand_text(file_size):
    txt_str = np.random.choice(np.frombuffer(letters, dtype='S1'), file_size)
    # print(txt_str)
    return txt_str


# 1KB files creation
for iter in range(0, num_one_kb_files):
    f = open("./tmpfs/one_kb_"+str(iter)+".txt", "wb")
    # specify file size
    f.write(get_rand_text(1000))
    f.close()
    

# 100 KB files creation
for iter in range(0, num_100_kb_files):
    f = open("./tmpfs/hundred_kb_"+str(iter)+".txt", "wb")
    # specify file size
    f.write(get_rand_text(100000))
    f.close()


# 1MB files creation
for iter in range(0, num_1_mb_files):
    f = open("./tmpfs/one_mb_"+str(iter)+".txt", "wb")
    # specify file size
    f.write(get_rand_text(1000000))
    f.close()

