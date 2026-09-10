"""HUAY DAK"""
a, b = input().upper().split()
z, x = input().upper().split()

if a == z and b == x:
    print(1000000)
elif a != z and b == x:
    print(100000)
elif b[2:] == x[2:] and a == z:
    print(2000)
elif b[2:] == x[2:] and a != z:
    print(200)
elif b[3:] == x[3:] and a == z:
    print(1000)
elif b[3:] == x[3:] and a != z:
    print(100)
elif a == z:
    print(20)
else:
    print(0)
