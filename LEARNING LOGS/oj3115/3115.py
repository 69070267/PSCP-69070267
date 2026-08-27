"""LEARNING LOGS"""
stores_at = [0] * 1442

num, _ = map(int, input().split())
for _ in range(num):
    start, stop = map(int, input().split())
    stores_at[start] += 1
    stores_at[stop] -= 1

current_stores = 0
active_stores = [0] * 1442
for minute in range(1441):
    current_stores += stores_at[minute]
    active_stores[minute] = current_stores

check_times = list(map(int, input().split()))

results = [str(active_stores[k]) for k in check_times]
print(" ".join(results))
