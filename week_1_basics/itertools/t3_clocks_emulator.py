from itertools import cycle
from itertools import product

class MyClock:

    def __init__(self):
        self._time_iterator = self._create_iterator()

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self._time_iterator)

    def _create_iterator(self):
        for t in product(range(24), range(60), range(60)):
            yield t

my_clock = MyClock()

for i in range(10000):
    time= next(my_clock)
    if i % 1000 == 0:
        print(f"{time[0]:02d}:{time[1]:02d} {time[2]:02d}.000")