import math


N = int(input())
M = math.ceil(math.sqrt(N)/2)

if M < 2:
    print(1)
    print(1)
    quit()

arr = [1]

for i in range(M-1):
    arr.append(math.floor(arr[-1] * 1.5) + 1)

print(M)
text = ""
for i in range(M):
    text += str(arr[i]) + " "
print(text[:-1])