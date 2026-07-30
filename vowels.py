num=input("Enter the string: ")

count=0
for ch in num.lower():
    if ch in "aeiou":
        count += 1

print(count)