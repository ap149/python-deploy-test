
import random
import string

def generate_id(length=24):
    characters = string.ascii_letters + string.digits 
    _id = ''.join(random.choice(characters) for i in range(length))
    return _id
