# Check Whether a Number is a Palindrome

# Input: 121
# Output: Palindrome
n=121
temp=n
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
    
if n==reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")