import math

c = 0
i = -1
b = 0
a = 0
fstep = True
while c != 2:
    i = i + 1
    if fstep:
        print ("?" + " " + str(0))
        fstep = not(fstep)
    else:
        print ("?" + " " + str(1))
    s = int(input())
    if s == 1:
        if c == 0:
            a = i
            c += 1
            i += math.floor((((a+1) / 2) + 1) ** 2) - math.floor(((a+1) / 2) ** 2)
            print("?" + " " + str(math.floor((((a+1) / 2) + 1) ** 2) - math.floor(((a+1) / 2) ** 2)))
            input()
        else:
            b = i
            c += 1
r = (b - a + 1) / 2
r = r * r
print("!" + " " + str(int(r - b)))