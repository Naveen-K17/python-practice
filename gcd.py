def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
    
n=int(input("Enter a number:"))
m=int(input("Enter another number:"))

print(gcd(n,m))