# Find the Largest Element in a List

# Input: [10, 45, 23, 89, 12]
# Output: 89


arr=[10, 45, 23, 89, 12]
largest=arr[0]

for i in arr:
    if i > largest:
        largest=i
        
print(f"The largest is {largest}")