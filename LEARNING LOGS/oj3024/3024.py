"""3024"""

summed = float(input())
maxxed = float(input())
#หมายความว่าคะแนนห่างจาก max มากเกินคือดูเหมือนหน้าม้า
minned = summed-(2*maxxed)

if  minned < 0:
    minned = 0

if maxxed -minned > 2:
    print("Surprising")
else:
    print("Not surprising")
