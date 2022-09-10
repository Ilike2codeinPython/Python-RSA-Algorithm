import random
#6n + 1 or 6n – 1
userin=int(input("How strong would you like your encryption to be?(Enter a number)\n"))
char=input("what would you like to encrypt\n")
charlist=list(char)
charlist2=[]
primes=[]
for u in range (3,userin + 3):
    x=0
    for i in range (1,u+1):
        primet=[]
        if u%i==0:
            primet.append("True")
        elif u%i!=0:
            primet.append("False")
        for z in primet:
            if z == 'True':
                x+=1
        #print (f"{x} = {u}")
        #print (primet)
        #print (f"i={i}")
        #print ("")
    if x <=2:
        primes.append(u)
print (primes)
primes=list(set(primes))
#print(primes)
primrange=primes[-1:]
pum=random.choice(primes)
qum=random.choice(primes)
num=(pum)*(qum)
pnum = int((pum-1)*(qum-1))
#primes.remove(pum)
#primes.remove(qum)
print (pnum)
while True:
    eum=random.choice(range(0,pnum))
    if eum in primes and eum !=pnum:
        break
print (eum)
dumnum=[]
dumn=[]
for i in range(eum,(eum**2)+1):
    dumn.append(i)
for i in dumn:
    print (f"i={i}")
    print (f"eum={eum}")
    print (f"eum^2={eum**2}")
    print (f"equation = {((i*eum)%pnum)}\n\n")
    if ((i*eum)%pnum)!=1:
        continue
    elif ((i*eum)%pnum)==1:
                dum = i
                dumnum.append(i)
print (dumnum)
#Choose two large prime numbers (p and q)
#print (pum, qum)
for e in charlist:
    charlist2.append(((ord(e)-96)**eum)%num)
print (f"Your Encryption key is ({eum},{num})")
print (f"your Encrypted message is: ", *charlist2)
print (f"The receiver key is({dum}, {num})")
input("Press 'Enter' to exit...")