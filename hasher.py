#!/usr/bin/python3
#large file
import hashlib # Built-in library for secure hashing algorithms 
path  = '/usr/txt/merlin/dictionaryAttack/dictionary1.txt'
def computeMD5hash(my_string):
    print(my_string)
    digest = hashlib.md5() 
    digest.update(my_string.strip().encode('utf-8')) 
    return digest.hexdigest()  

with open(path) as f:
    for i in range(61267100):
        next(f)
    for line in f:
        print(line)
        dic_hash = computeMD5hash(line)
        print(dic_hash)
        if dic_hash == "3a8b7b53ab2be90f457869961f475aab":
            print("Correct\(line)",dic_hash,line)
            break

