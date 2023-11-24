import time

x = int(input("Entrez un nonbre n : "))

for i in range(x, 0, -1):
    print(i)
    time.sleep(1)


y = int(input("Entrez un nonbre n : "))

while y > 0:
    print(y)
    y -= 1
    time.sleep(1)
