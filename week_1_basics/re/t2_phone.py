import re

# Suppose that number should start with "+" and have 5 digits
PHONE_PATTERN = r'^\+[\d]{5}$'

test_strings = '+12345 +123 +23 +1234 +05 +ddd +1d +99999 +123456'.split()

print(test_strings)

for phone in test_strings:
    if re.match(PHONE_PATTERN, phone):
        print(f'Phone number {phone} is vaid!')
