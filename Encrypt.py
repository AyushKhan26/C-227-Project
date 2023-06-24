print('Welcome')
print('Rules: dont open it')

message = input('Enter the message to be encrypted: ')
key =  input('Enter encryption key(At least 8-digit): ')
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "

encrypted_text = " "

for i in message:
    position = alphabet.find(i)
    newposition = (position + int(key))%94
    encrypted_text = alphabet[newposition]
    
    output = (encrypted_text)
 

print("Encrypted Text: "+ (output))
print("Encryption key: "+ (key))
