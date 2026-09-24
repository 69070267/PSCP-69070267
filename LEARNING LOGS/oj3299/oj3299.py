"""LLoj3299"""
L, N = map(int, input().split())
d = 1
while True:
    k = d * L
    total_cells = (k * (k + 1)) // 2
    if N <= total_cells:
        print(d)
        break
    d += 1
