print('Welcome')
print('Rules: Dont Open it')

import random
for i in range(1):
    keygen = (random.randint(11111111111, 999999999999999))

message = input('Enter message to be decrypted: ')
key = input('Enter encryption key: ')
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ"

decrypted_text = ' '

for i in message:
    position = alphabet.find(i)
    newposition = (position - int(key))%94
    decrypted_text = alphabet[newposition]
    
    output = (decrypted_text)

keyout = (keygen)

print('Decrypted message: '+ (output))


