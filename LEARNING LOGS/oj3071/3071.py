"""AB"""
A = int(input())
B = int(input()) #B > A
d = int(input())
r = int(input()) #r<d

count = 0
for x in range(A, B + 1):
    if x % d == r:
        count += 1
print(count)
