"""temp"""
tempN = float(input())
tempA = input()
tempZ = input()
tempOUTPUT = 0.0
if tempA == tempZ:
    tempOUTPUT = tempN
# C
elif tempA == "C" and tempZ == "K":
    tempOUTPUT = tempN + 273.15
elif tempA == "C" and tempZ == "F":
    tempOUTPUT = (tempN * 9/5) + 32
elif tempA == "C" and tempZ == "R":
    tempOUTPUT = (tempN + 273.15) * 9/5
# F
elif tempA == "F" and tempZ == "C":
    tempOUTPUT = (tempN - 32) * 5/9
elif tempA == "F" and tempZ == "K":
    tempOUTPUT = (tempN - 32) * 5/9 + 273.15
elif tempA == "F" and tempZ == "R":
    tempOUTPUT = tempN + 459.67
# K
elif tempA == "K" and tempZ == "C":
    tempOUTPUT = tempN - 273.15
elif tempA == "K" and tempZ == "F":
    tempOUTPUT = (tempN - 273.15) * 9/5 + 32
elif tempA == "K" and tempZ == "R":
    tempOUTPUT = tempN * 9/5
# R
elif tempA == "R" and tempZ == "C":
    tempOUTPUT = (tempN - 491.67) * 5/9
elif tempA == "R" and tempZ == "F":
    tempOUTPUT = tempN - 459.67
elif tempA == "R" and tempZ == "K":
    tempOUTPUT = tempN * 5/9
print(f"{tempOUTPUT:.2f}")
