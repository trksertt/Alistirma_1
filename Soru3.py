x = 0
for i in range (1,999):
    y = 1
    for z in range (1,i):
        y *= z
    x += 1/y
print(x)
