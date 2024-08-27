# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> Hash functions share different properties, they are one way, and they will always return the same output when the same key / parameter is used, they take key of any length, produce an output of an fixed length, they should be short / effiecent to compute, and should be improssible to invert the returned value.

Source - https://www.sciencedirect.com/topics/computer-science/hashing-algorithm#:~:text=Besides%20being%20one%2Dway%2C%20hash,have%20some%20other%20basic%20properties%3A&text=They%20take%20an%20input%20of,output%20of%20a%20fixed%20length.&text=They%20should%20be%20efficient%20and%20fast%20to%20compute.&text=They%20should%20be%20computationally%20infeasible%20to%20invert.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> 1. the first hash function always will return the same value, leading to zero collision reisistance, and will not change regardless of what key is used,

> 2. The second is very simple to impliment, is generally pretty uniform, is very efficient as its simple design can be quick to compute, has medium collission resistance, it is better than the simple hash function, however collision resistance is still quite low, is very sesitive to change as even small input changes can alter the output, security would be rather low as collision chance is still high

>3. The third is an bit more complex than the second option, it is generally uniform, it is still rather efficient however not as efficient as the last, Has an good resistance to collisions however not as good as more complex hash functions, is sensitive to small changes as small changes can significantly change the output, is decently secure, and prodeuces an randomlike hash, due to using the random module.

>Resources - https://en.wikipedia.org/wiki/Pearson_hashing

>4. is decent however is depended on the object, is optimised for various python objects / classes, can offer reasonable collision resistance, sensitive to small changes, can offer medium security

>Resources - https://www.codecademy.com/resources/docs/python/built-in-functions/hash

>5. The SHA256 hash is an excellent at uniformity, is efficient, but less efficient, than all of the previous hash functions, has an excellent collission resistance, is very sensitive to small changes, due to its encryption and is secure.

>Resources - https://www.n-able.com/blog/sha-256-encryption

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> Determinism, an hash should always return the same value for an specific key, without this is cannot be used in many applications such as for hash tables as it would not be reliable, Uniformity, distrubuted evenely across an output range can help to avoid collisions, and evenly produce values, Efficiency, this is important in hash functions as depending on the size of the key / hashmap, can affect performance of the application, large inputs can significantly slow down operations.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> Pearson hash function, more complex than the two simplest hash, used as has an decent average accross all attributes, i thought has better collision resistance than the simple hash function and the ASCII hash function, however was still reletively simple compared to the SHA256, and did not need import.


5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> imports the random library, then sets an fixed seed for the generator, creates an pearson_table with the values from 0 - 255, shuffles the list, takes an key / size, initialises hash_ as 0, iterates over each character in the key, for each character(char) it sets the hash_ variable to the value of the pearson_table with the index of _hash ^ the current char as unicode

then returns an remainder of hash_ / the size

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

```python
# initialise the hashmap
# 
# Create an function for get that takes an key and an value
# Run the hash finction on the key

# item = hashmap[index]
# try:
#   item = item.find(key)
#   
#   item.uid = value
# except:
#   item.push(Player(key, value))
#
#
```

## Reflection

1. What was the most challenging aspect of this task?

> Learning about / implimenting the hashmaps, and the differences between them, some hashmaps are simlper than others, however some can get quite complex, with hashes as SHA256 using cryptography / encryption to ensure high security, and outputs an hash of 256 bits long

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> I would have either used an list / array, this can provide an simlier soution to the linked list and is built directly into

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
