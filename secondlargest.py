# Find the second largest element in a list
lists=[1,2,3,5,50,10]
# largest=lists[0]
# for num in lists:
#     if(num>largest):
#         largest=num
# print(largest)
lists.sort()
print(lists[-2])