import re

VALID_EMAILS = 'firstvalid@gmail.com secondvalid@gmail.com thirdvalid@gmail.com'
VALID_EMAIL = 'firstvalid@gmail.com'
LETTER_CONTENT = 'Hello, test@gmail.com! I am very glad to see your collegue john@gmail.com and you.'
EMAIL_PATTERN = r'\b[\w\-\.]+@(?:[\w-]+\.)+[\w\-]{2,4}\b'

emails = re.findall(EMAIL_PATTERN, LETTER_CONTENT, re.MULTILINE)

print(emails)
