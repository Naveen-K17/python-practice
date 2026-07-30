def binarysearch(arr,target):
    low = 0
    high = len(arr)-1
    
    while low<=high :
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
number=[1,2,3,4,6,55]
target=55

result=binarysearch(number,target)

if result!=-1:
    print(f"the element found at index {result}")
else:
    print("not found")
    