"""RED GREEN BLUE"""
r1, g1, b1 = map(int, input().split())
r2, g2, b2 = map(int, input().split())

rnew = (r1 + r2) // 2
gnew = (g1 + g2) // 2
bnew = (b1 + b2) // 2

print(rnew, gnew, bnew)
