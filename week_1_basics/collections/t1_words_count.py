import sys
from collections import defaultdict

if len(sys.argv) != 2:
    print("Usage: py -3 t1_words_count.py <file_name>")
    sys.exit(1)

to_split = [',', '.', '!', '?', ':', '...']
words = defaultdict(int)

try:
    with open(sys.argv[1], encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print("Error: no file with name: " + sys.argv[1] + "1")
    sys.exit(1)

for sep in to_split:
    text = text.replace(sep, ' ')

text_lst = text.split()

for word in text_lst:
    words[word] += 1

for k,v in words.items():
    print('Word "' + k + '" occurred ' + str(v) + ' times in the text!')
