a=int(input("Enter a Prime Number - a = "))
b=int(input("Enter a Prime Number - b ="))

if (a==b):
    print("For RSA a should not be eual to b")
    exit
else:
    n=a*b
    q=((a-1)*(b-1))

def computeGCD(e, q):
 
    if e > q:
        small = q
    else:
        small = e
    for i in range(1, small + 1):
        if((e % i == 0) and (q % i == 0)):
            gcd = i
             
    return gcd    
e=int(input("Enter Value for 'e' such that GCD of (e,q)=1::"))
gcd= computeGCD

if (gcd !=1):
    print("GCD of e,q for RSA should be 1")
    exit

i