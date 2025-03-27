from collections import Counter
from random import randint

nums = [randint(1, 100) for i in range(10000)]

c = Counter(nums)

mc_number = tuple(*c.most_common(1)) # most_common returns list of tuples. I only need one tuple
print(f"Number {mc_number[0]} if most-common and occurred {mc_number[1]} times")
