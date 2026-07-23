""""IF ELSE ELIF"""
def main():
    """IF ELSE ELIF"""
    COLORONE = input().strip().capitalize()
    COLORTWO = input().strip().capitalize()
    if COLORTWO == COLORONE and COLORONE in {"Red","Yellow","Blue"}:
        print(COLORONE)
    elif COLORONE == "Red" and COLORTWO == "Yellow":
        print("Orange")
    elif COLORONE == "Yellow" and COLORTWO == "Red":
        print("Orange")
    elif COLORONE == "Red" and COLORTWO == "Blue":
        print("Violet")
    elif COLORONE == "Blue" and COLORTWO == "Red":
        print("Violet")
    elif COLORONE == "Yellow" and COLORTWO == "Blue":
        print("Green")
    elif COLORONE == "Blue" and COLORTWO == "Yellow":
        print("Green")
    else:
        print("Error")
main()
