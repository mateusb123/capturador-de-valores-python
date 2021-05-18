import string
from random import random, choice

code = input("code:")

if 'randomPassword' in code:
    if '(' in code:
        n = code.find('(')
        number = ""
        for c in range(code.find(')')):
            if code[c] == ')':
                break
            elif code[c] == '(':
                while code[c] != ')':
                    number += code[c+1] 
                    c+=1

        values = string.ascii_letters + string.digits
        password = ""
        number = int(number.replace(')',''))
        for p in range(number):
            password += choice(values)

        print('password: ' + password)
