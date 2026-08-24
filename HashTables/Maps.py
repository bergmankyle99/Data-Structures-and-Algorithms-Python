#Hashmaps are dictionaries in python
d = {"kyle": 1}
print(d)

#add key:val to hashmap (dictionary) O(1)
d["josh"] = 2
print(d)

#check if key in dicitionary O(1)
if "kyle" in d:
    print(True)
    # check value corresponding to key in dictionary
    print(d["kyle"])

#loop over key:val pairs in dicitonary: O(n)
for key, val in d.items():
    print(f"{key}:{val}")

#defaultdict
from collections import defaultdict
default = defaultdict(list)
print(default[2])

#counter
from collections import Counter
counter = Counter("aaaaaaabbbbbbbccccccc")
print(counter)