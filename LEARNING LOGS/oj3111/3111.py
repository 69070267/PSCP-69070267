"""SAHAKORN"""
import math
member = str(input())
itemslists = int(input())
pricetotal = 0
for _ in range(itemslists) :
    prices = float(input())
    pricetotal+=prices
if member == "Y" :
    fivepercent = pricetotal-(pricetotal*0.05)
    roundedup = math.ceil(fivepercent*100)/100
    print(f"{roundedup:.2f}")
elif member == "N" and pricetotal >= 500 :
    threepercent = pricetotal-(pricetotal*0.03)
    roundedup = math.ceil(threepercent*100)/100
    print(f"{roundedup:.2f}")
else :
    print(pricetotal)
