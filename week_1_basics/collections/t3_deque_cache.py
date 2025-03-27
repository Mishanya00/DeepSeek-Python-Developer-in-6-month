from collections import deque


class CacheObject:

    def __init__(self, value):
        self.value = value

class DequeCache:

    def __init__(self, capacity):
        self._capacity = capacity
        self._elements = deque()

    def add(self, obj: CacheObject):
        if len(self._elements <= self._capacity):
            self._elements.append(obj)
        else:
            self._elements.popleft()
            self._elements.append(obj)