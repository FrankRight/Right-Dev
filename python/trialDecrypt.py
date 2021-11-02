sms = '108109110111'
decrypted_message = []


def string_to_list(message_string):
    list1= [message_string[i:i+3] for i in range(0, len(message_string), 3)]
    return list1

sms = string_to_list(sms)

print(sms)

for i in sms:
    print(i)
    to_be_appended_char = str(int(i)-ord(','))
    append_char = chr(int(to_be_appended_char))

    decrypted_message.append(append_char)
    print(decrypted_message)

def list_to_string(message_array):   
    str1 = "" 
  
    for element in message_array: 
        str1 += str(element)
  
    return str1

def Reverse (string_to_be_reversed):
    return ((string_to_be_reversed[::-1]))

message = Reverse(decrypted_message)

print(decrypted_message)
print(list_to_string(message))
