import re
import sys

filename = input('File with text: ')

try:
    with open(filename, encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print('Non-existing filename error!')
    sys.exit(1)

print('- - - - - - - -Text from file - - - - - - - - ')
print(text)
print('- - - - - - - - - - - - - - - - - - - - - - - ')

old_word = input('Word to change: ')
new_word = input('New word: ')

pattern = r'\b' + old_word + r'\b'
print('PATTERN:', pattern)
text = re.sub(pattern, new_word, text)

print('- - - - - - - - New text - - - - - - - - ')
print(text)
print('- - - - - - - - - - - - - - - - - - - -- ')
