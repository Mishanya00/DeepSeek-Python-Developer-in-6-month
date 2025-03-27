from collections import deque


class DequeCache:

    def __init__(self, capacity):
        self._capacity = capacity
        self._elements = deque()

    def __getitem__(self, index):
        res = self._elements[index]
        self._elements.remove(self._elements[index])
        self._elements.append(res)
        return res
    
    def __repr__(self):
        return ', '.join(list(map(str, self._elements)))

    def add(self, obj):
        if obj in self._elements:
            self._elements.remove(obj)
            self._elements.append(obj)
        else:
            if len(self._elements) <= self._capacity:
                self._elements.append(obj)
            else:
                self._elements.popleft()
                self._elements.append(obj)

cache = DequeCache(5)

for i in range(20):
    print(cache)
    cache.add(i)

print(cache)

print('Here is get:')
cache[2]
print(cache)
cache[2]
print(cache)
cache[2]
print(cache)