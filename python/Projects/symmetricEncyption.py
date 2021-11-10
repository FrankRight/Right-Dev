from cryptography.fernet import Fernet


# Generate the secret key to be used
secretKey = Fernet.generate_key()
encoded = Fernet(secretKey)

# Encrypting using python function 
def encrypt_text(plain_text):
    return encoded.encrypt(bytes(plain_text, "UTF-8")).decode()


# Decrypting using python function
def decrypt_text(cypher_text):    
    return encoded.decrypt(bytes(cypher_text,"UTF-8")).decode()


# Main encrypt and decrypt app
def app():
    # User input of the message
    plain_text = input("Enter the message you will like to Encypt:- ")

    # Message processing
    cypher_text = encrypt_text(plain_text)
    print("\n\nEncrypted message that will be sent \n %s" %(cypher_text))

    decrypted_text = decrypt_text(cypher_text)
    print("\n\nDecrypted message at the receiver's end \n %s" %(decrypted_text))

# Call the app
app()