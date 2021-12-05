import math, hashlib

def spacing():
    print("\n\n\n")
 
print("RSA ENCRYPTOR/DECRYPTOR ")
spacing()
 
# Input Prime Numbers
print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
spacing()
 
# A function that checks if inputs are prime or not
def prime_check(a):
    if(a==2):
        return True
    elif((a < 2) or ((a%2) == 0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True

# Use the above function with the inputted values by user
check_p = prime_check(p)
check_q = prime_check(q)

# If false prompt the user for other p and q values
while(((check_p==False)or(check_q==False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)
 
# calculate the modulus(n) of p and q (the 2 prime numbers)
n = p * q

# Print the modulus(n) value of the RSA
print("RSA Modulus(n) is:", n)
 
# Calculate and print Eulers Toitent(r)
r= (p-1) * (q-1)
print("Eulers Toitent(r) is:", r)
spacing()
 
# Function to calculate the GCD
def egcd(e, r):
    while(r != 0):
        e,r=r,e%r
    return e
 
# Function representing Euclid's Algorithm
def eugcd(e, r):
    for i in range(1, r):
        while(e != 0):
            a,b = r//e,r%e
            if(b != 0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b
 
# Function extending the Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
# Multiplicative Inverse Function
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s = %d. Since %d is less than 0, s = s(modr), i.e., s = %d."%(s,s,s%r))
        elif(s>0):
            print("s = %d."%(s))
        return s%r
 
# Calculate the co-prime(e)
for i in range(1,1000):
    if(egcd(i,r) == 1):
        e = i
print("The co-prime value is:", e)
spacing()

# Finding the Private and Public Keys
print("Euclid's Algorithm\n START")
eugcd(e,r)
print("END")
spacing()

print("Euclid's EXTENDED ALGORITHM\nSTART")
d = mult_inv(e,r)
print("The value of multiplication inverse is:",d)
print("END")
spacing()

public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
spacing()
 
# Function of the encrypting algorithm
def encrypt(pub_key,n_text):
    e,n = pub_key
    x = []
    m = 0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c = (m**e)%n
            x.append(c)
        elif(i.islower()):               
            m = ord(i)-97
            c = (m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     
 
# Function of the decrypting algorithm
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i == '400'):
            x.append(' ')
        else:
            m = (int(i)**d)%n
            m += 65
            c = chr(m)
            x += c
    return x
 
#Message
message = input("Type the message to be decypted?(Separate numbers with ',' for decryption): ")
print("Your message is:", message)
 
#Choose Encrypt or Decrypt and Print
choose = input("Type 1 for encryption and 2 for decrytion. ")

if(choose == '1'):
    enc_msg=encrypt(public,message)
    print("Your encrypted message is:",enc_msg)

elif(choose == '2'):
    print("Your decrypted message is:",decrypt(private,message))

else:
    print("You entered the wrong option. TRY AGAIN")