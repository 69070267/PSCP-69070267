"""IF ELSE AGAIN"""

def main():
    """IF ELSE AGAIN"""
    loca = input()
    kg = float(input())
    if loca == "BKK CNX" :
        calculated = (30*kg)+10
        print(f"{calculated:.2f}")
    elif loca == "CNX UBP" :
        calculated = (40*kg)+15
        print(f"{calculated:.2f}")
    elif loca == "UBP BKK" :
        calculated = (40*kg)+20
        print(f"{calculated:.2f}")
    elif loca == "BKK PKT" :
        calculated = (50*kg)+25
        print(f"{calculated:.2f}")
    elif loca == "PKT CNX" :
        calculated = (60*kg)+30
        print(f"{calculated:.2f}")
    elif loca == "UBP PKT" :
        calculated = (70*kg)+40
        print(f"{calculated:.2f}")
    else :
        print("Error")
main()
