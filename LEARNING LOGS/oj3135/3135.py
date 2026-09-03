"""31355313"""
N, K, T = map(int, input().split())
count = 1
curr = 1
if T == 1:
    print(count)
else:
    while True:
        curr = (curr + K - 1) % N + 1
        if curr == T:
            count += 1
            break
        if curr == 1:
            break
        count += 1
    print(count)
