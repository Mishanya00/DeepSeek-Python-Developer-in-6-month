import logging
from random import randint

def function():
    return randint(1, 1000)

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
