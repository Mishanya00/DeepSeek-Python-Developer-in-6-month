from itertools import permutations

lst = list(map(int, input('List to get permutations: ').split()))

res = [el for el in permutations(lst)]

if len(res) < 200:
    print('All possible permutations:')
    for el in res: print(el)
else:
    print(f'Count of permutations: {len(res)}')
