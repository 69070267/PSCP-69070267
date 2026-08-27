"""LEARNING LOG WHILE LOOP?"""
a = int(input())
b = int(input())
goal = int(input())

usableB = min(b, goal // 5)
remains = goal-(usableB * 5)

if remains <= a :
    print(remains)
else :
    print("-1")
