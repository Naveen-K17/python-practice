# string=input("Enter a string")

# count=0
# for ch in string.lower():
#     if ch in "aeiou":
#         print(ch, end="")
# lists=[1,20,20,1]

# result=list(set(lists))
# print(result)
             # 0112358

# n=3
# a=0
# b=1

# for i in range(n):
#     print(a, end=" ")
#     a,b=b,a+b
# list=[10,20,30,10,20]

# sum=0
# for num in list:
#     sum=sum+num
    
# print(sum)
# a=10
# b=20
# a=b
# b=a
# print(a)
# print(b)
# number=0
# sum=0
# while number>0:
#     digit=number%10
#     sum=sum*10+digit
#     number=number//10
# print(sum)
# num=121
# reverse=0
# temp=num
# while temp>0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp=temp//10

    
# if reverse==num:
#     print("palindrome")
# else:
#     print("Not palindrome")
# lists=[10,20,10,50,40]

# largest=lists[0]
# for num in lists:
#     if num>largest:
#         largest=num
        
# print(largest)
# num=int(input("Enter a number"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")
# def linearsearch(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1
# number=[10,20,40,30]
# target=40
# print(linearsearch(number,target))
# n=123456789123456789
# count=0
# while n>0:
#     digit=n%10
#     count+=1
#     n=n//10
# print(count)
# n=3
# a=0
# b=1
# for i in range(n):
#     print(a, end=" ")
#     a,b=b,a+b
# string="hello"
# reverse=string[::-1]
# print(reverse)

n=12345

reverse=0

while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)