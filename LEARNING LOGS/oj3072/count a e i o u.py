"""learning logs count AEIOU"""
TEXT = str(input().lower())
vowels = ['a','e','i','o','u']
for i in vowels:
    count = TEXT.count(i)
    if count > 0:
        print(f"{i} : {count}")
