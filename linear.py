def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

num=[1,2,3,4,5,6,7]
target=8

result=linearsearch(num,target)

if result!=-1:
    print(f"The element is found at index {result}")
else:
    print("The number is not found")