"""31603160"""
a,b = map(int, (input().split()))
primes = []
for i in range(a, b+1):
    if i > 1 and all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
        primes.append(i)
if len(primes) > 0 :
    print(*primes)
    print(f"Total primes: {len(primes)}")
else :
    print(f"Total primes: {len(primes)}")
