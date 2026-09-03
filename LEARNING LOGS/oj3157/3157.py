"""learning logs"""
N = int(input())
count = 0
for _ in range(N) :
    X = str(input())
    if X == "+" :
        count += 10
    elif X == "-" :
        count -= 5 
    else :
        count += 0 
print(count)
