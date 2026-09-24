"""กรอบเบิ้มๆ"""
wrdlst = []
lngth = 0
for i in range(5):
    words = str(input().rstrip())
    wrdlst.append(words)
    if len(words) >= lngth :
        lngth = len(words)
print("**"+("*"*lngth)+("**"))

for word in wrdlst:
    print("* " + word.ljust(lngth) + " *")

print(("**"+ ("*" * lngth))+("**"))
