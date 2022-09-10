userin=input("What is your RSA message?")
mesencr=userin.split()
decr=[]
##print (mesencr)
enckey=int(input("What is the first value in your key"))
encvalue=int(input("What is the second value in your key"))

for i in mesencr:
    decrkey=(int(i)**enckey)%encvalue
    if decrkey > 26:
        decr.append(" ")
    else:
        decr.append(chr(decrkey+96))
print ("your decrypted string is:",*decr)
input("Press 'Enter' to exit...")