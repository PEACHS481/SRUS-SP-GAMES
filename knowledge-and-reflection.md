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

> The hash functions above all have the key and size parameter, where key is the string passed 
> through the function and size is the hash tables size. 
> The key properties of hash functions, are deterministic, fixed output size, efficiency, uniformity and avalanche effect.
> Deterministic: the hash function can produce the same output with the identical input. this allows for anyone using the input to get the identical output.
> Fixed output size: all hashes have a fixed output size respective to their hash function, so their output is fixed regardless of input size.
> Efficiency: the hash functions are not overly complex, and the process of the input to output is quick.
> Uniformity: Some of these have their hash values spread across the output space evenly, avoiding similar values between outputs. 
> Avalanche Effect: small changes in the input can result in the output being unpredictable and different.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> The four main hash functions above are the ASCII hash, Pearson hash, python's built-in hash function and SHA-256 hash.

> ASCII hash positives are that it is very efficient as it's just getting the sum from the hash key. the hash function is also good in terms of determinism as the same input will give the same sum. it's also simple to use and implement.
> ASCII hash negatives is that there is little uniformity as inputs can often give the same output. As a result, the collision resistance is low. ASCII is also quite weak for sensitivty as the change in a small input can result in a small change of the output. this can be concerning for the security the hashmap stores.

> Pearson hashes benefits are the uniformity of inputs, efficiency as its faster than other hash methods, sensitivity as any small changes can create a drastically different output and has a little bit of collision resistance, which is good for smaller hashmaps.
> Pearson hashes negatives are that the 

> Python's hash benefits are that it is very efficient and has good uniformity, also the sensitivity is better than the ASCII hash function
> > Pythons's hash negatives is the determinism is not good, as the hash seed python uses is randomized when each session is started. This can allow for the collision resistance to be low.

> SHA-256 hash positives are the uniformity is good as the values are spread throughout evenly, so the lists can fill up evenly. Determinism is strong as the same input string gives the correct output value. The collision resistance is strong as long as there is many containers. Sensitivity is very strong, the input being changed results in the output value being very different. security risks are a bit lower compared to other hashes.
> SHA-245 hash negatives are for efficiency it can be slow and is more suited towards larger hashmaps. 

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> Your answer here

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> Your answer here

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> Your answer here

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> Your answer here

## Reflection

1. What was the most challenging aspect of this task?

> Your answer here

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> Your answer here

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
