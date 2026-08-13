"""math , map , split , for loop"""
import math
S,N = map(int, input().split())
PI = 3.1416
results = []
for _ in range(N) :
    x, y = map(int, input().split())
    circleArea = PI * (x**2 + y**2)
    timer = circleArea / S
    results.append(math.ceil(timer))
for ans in results :
    print(ans)
