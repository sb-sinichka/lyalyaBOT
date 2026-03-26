import random

def gen_pass(length):
    alphabet = "1234567890!%#&?_abcdefgehABCDEFGH"
    result = ""

    for i in range(length):
        result += random.choice(alphabet)


    return result