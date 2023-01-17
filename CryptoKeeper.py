# Encryption function
def encryptor(message): 
 
    # create an empty list to store the encrypted message
    encrypted_message = [] 
  
    # loop through the message
    for letter in message: 
  
        # store the encrypted letter in the list 
        encrypted_message.append(chr(ord(letter) + 1)) 
  
    # join all the encrypted letters together 
    encrypted_message = ''.join(encrypted_message) 
  
    # return the encrypted message 
    return encrypted_message 
  
# Driver code 
message = input('Enter a message to encrypt: ') 
print('Encrypted message:', encryptor(message))
