for x in range(1,2005):
    y = 0
    for z in range(len(str(x))):
        y += int(str(x)[z])
    if y == 2005- x :
        print(x)
