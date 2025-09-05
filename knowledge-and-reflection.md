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
> Pearson hashes negatives are that it is not cryptographically secure, which for security reasons is not recommended. The effectiveness is based upon thie size of the lookup table. there are also collision risks.
> [1] 

> Python's hash benefits are that it is very efficient and has good uniformity, also the sensitivity is better than the ASCII hash function
> Pythons's hash negatives is the determinism is not good, as the hash seed python uses is randomized when each session is started. This can allow for the collision resistance to be low.
> [2]

> SHA-256 hash positives are the uniformity is good as the values are spread throughout evenly, so the lists can fill up evenly. Determinism is strong as the same input string gives the correct output value. The collision resistance is strong as long as there is many containers. Sensitivity is very strong, the input being changed results in the output value being very different. security risks are a bit lower compared to other hashes.
> SHA-245 hash negatives are for efficiency it can be slow and is more suited towards larger hashmaps. 
> [3]

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> The three most important attributes are for the hashmap are determinism, effciency and uniformity.
> I have chosen these attributes as regardless of the size of the hashmap these three would be most desirable. 
> Determinism is the most important as you would always want the same input to retrieve and give the same output. this is unless you want a change in the output for security reasons like the python built-in hash function.
> Effciency as you want the process to be quick and easy to get to the output. for larger hashmaps, security could be a bigger requirement then efficiency. As the hashmap here is small, the need efficiency is higher.
> Uniformity is the third most important attribute as you want keys to spread evenly to all the player lists. This is so that one list doesn't have many more values contained then another and prevent clustering.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> For the tasks requirements, I have went with the ASCII hash function. This because the size of the hashmap is very small and is efficient. another benefit is for learning purposes, as that its easy to understand on how the input is changing the output.
> There is also good determinism as the same input always gives the same output. as the hashmap size is small, The ASCII hash is good for testing and better understanding on how hashmaps work.
> there can be collisions and the clustering is often as a small change in the output leads to a small change for the output.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> import random imports the python random module.
> random.seed(42) allows for rerunning of the code to be the same seed so the outputs will be the same.
> the incorrect commented code allows the pearson_table to get random integers between 0 and 255. this can allow for repeat integers or some might not even be in the table.
> pearson_table = list(range(256)) sets up the pearson table and gives a list of each int from 0 to 255. this is efficient as its only got 256 possible indexes for the hashmap.
> random.shuffle(pearson_table) is rearranging the order of the table.
> def pearson_hash(key: str, size: int) -> int: sets up the function that takes a key to be hashed and the size of the hashmap
> hash_ = 0 starts the hash value to 0.
> for char in key: will go through each character in the key string.
> ord(char) will get the character and convert into ASCII integer code. as its doing it for each char,  the sensitivity is high as it can create very different outputs 
> hash_ ^ will add the ord(char) to the hash_
> pearson_table gets the result and uses it as an index in the table
> it is then saved as the hash_
> return hash_ % size will get the number of the hash_ and will return it according to the size of the hashmap range

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> PlayerHashMap (size = 10)
> function init:
>   hashmap = new PlayerHashMap
> 
> function set_item(hashmap, uid, name):
> 
>   index = my_hash_function(uid, hashmap.size)
> 
>   playerlist = hashmap._mapping(index)
> 
>   current_node = playerlist.head
>    while !current_node.is_empty:
>       if current_node.player.uid == uid
>        current.player.name = name
>        return
>    current = current.next_node
> 
>   added_player = Player(uid, name)
> 
>   playerlist.append(aded_player)

## Reflection

1. What was the most challenging aspect of this task?

> Most challenging aspect of the task was understanding how the hashes work and can be used with our current linked lists. that is why I chose the ASCII hash as its easy to understand and simple to debug/ go through step by step.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> if I didnt use a playerlist, i would experiment with other hashes and other collision resolution methods. I would for example maybe have a larger hashmap and use SHA-256 hash. 
> I could also implement a method for containers like the playerlist, to have a resize function. so when a item gets added and reaches a limit of items added in that container, to resize and create a bigger array.

## Reference
[1]. Pearson Hashing in Python. https://mojoauth.com/hashing/pearson-hashing-in-python/

[2]. Python hash() method. https://www.geeksforgeeks.org/python/python-hash-method/

[3]. Is SHA-256 secure? Legal & Compliance Experts Say Yes—Here’s Why https://blog.pagefreezer.com/sha-256-benefits-evidence-authentication

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
