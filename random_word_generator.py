import random
import string

def randomwords(length=5):
    letters = string.ascii_lowercase
    randomword = ''.join(random.choice(letters) for x in range(length))
    return randomword

randomword = randomwords()
print(randomword)
