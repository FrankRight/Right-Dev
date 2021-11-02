import time

def Reverse (string_to_be_reversed):
    return ((string_to_be_reversed[::-1]))

def list_to_string(message_array):  
    str1 = ""
  
    for element in message_array:
        str1 += str(element)
  
    return str1

def string_to_list(message_string):
    list1 = message_string.split()
    
    return list1

def Encrypt(sms):
    reversed_string = Reverse(sms)
    encrypted_message = []

    for i in reversed_string:
        append_char = str(ord(i)+ord(','))+ " "
        encrypted_message.append(append_char)

    return encrypted_message

def Decrypt(sms):
    decrypted_message = []
    sms2 = string_to_list(sms)
    for i in sms2:
        to_be_appended_char = str(int(i)-ord(','))
        append_char = chr(int(to_be_appended_char))
        decrypted_message.append(append_char)

    decrypted_message = list_to_string(decrypted_message)
    message = Reverse(decrypted_message)

    return message

def loading_function(message):
    print(message)
    time.sleep(1)
    print(" .")
    time.sleep(1)
    print("  .\n")
    time.sleep(1)

def Encrypt_decypt_app ():
    print("#### SENDER ####\n")
    name = input("Enter the sender name: ")
    message = input("Enter a message (Press Enter to send): ")
    encrypted_message = list_to_string(Encrypt(message))

    encrypted_sender_name =list_to_string(Encrypt(name))

    print("\nuser '", encrypted_sender_name, "' your message was encryped as: '", encrypted_message, "'")

    loading_function('\nSending\n')

    print("Message sent\n\n")
    time.sleep(2)

    print("\n\n#### RECEIVER ####\n")

    print("You have a new message.\n")
    print("The message: ", encrypted_message, "\n\nFrom User, ", encrypted_sender_name)

    loading_function("\n\nDecrypting the message\n.")

    decrypted_sender_name = Decrypt(encrypted_sender_name)
    decrypted_message = Decrypt(encrypted_message)

    print(decrypted_sender_name, " has sent you this message: ", decrypted_message)

Encrypt_decypt_app()
