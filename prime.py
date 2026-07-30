# Check Whether a Number is Prime

# Input: 17
# Output: Prime
num=17
if num>=1:
    for i in range(2,num):
        if num%i==0:
            print("Not a prime")
            break
    else:
        print("It is a prime")
else:
    print("not a prime")