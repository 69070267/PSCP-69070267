"""FROG FRGGGGGGGGGGG"""
X, Y = map(int, input().split())
distance = 0
count = 0
while X > 0 and distance < Y:
    distance += X
    count += 1
    X -= 2
if distance >= Y:
    print(count)
else:
    print(-1)
