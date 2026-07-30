# Find the LCM of two numbers
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def LCM(a,b):
    return (a*b) // gcd(a,b)

num1=int(input())
num2=int(input())

print(LCM(num1,num2))