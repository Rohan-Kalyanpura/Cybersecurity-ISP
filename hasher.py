#!/usr/bin/python3
#large file
import hashlib
path  = '/usr/txt/merlin/dictionaryAttack/dictionary1.txt'
file1 = open('/usr/txt/merlin/dictionaryAttack/dictionary1.txt', 'r')
count = 0
def computeMD5hash(my_string):
    print(my_string)
    m = hashlib.md5()
    m.update(my_string.strip().encode('utf-8'))
    return m.hexdigest()

import itertools
with open(path) as f:
    for i in range(61268100):
        next(f)
    for line in f:
        print(line)
        dsd = computeMD5hash(line)
        print(dsd)
        if dsd == "3a8b7b53ab2be90f457869961f475aab":
            print("Correct\(line)",dsd,line)
            break

