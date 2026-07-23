""""LEARNING LOG BILLS"""
import math
def main():
    """LEARNING LOG BILLS"""
    price = int(input())
    if (price*0.1) <= 50:
        price += 50
    elif (price*0.1) >= 1000:
        price += 1000
    else:
        price += price*0.1
    print(f"{price + (price*0.07):.2f}")
main()
