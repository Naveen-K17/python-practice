# Count digits in a number
num=12345
count=0
if num==0:
    count=1
else:
    num=abs(num)
    while num>0:
        count+=1
        num //=10
print(count)