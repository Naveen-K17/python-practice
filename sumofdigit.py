# Find the sum of digits of a number
n=int(input())

sum=0
n=abs(n)
while n>0:
    digit=n%10  #gets last element
    sum+=digit
    n//=10     # remove last element
print(sum)