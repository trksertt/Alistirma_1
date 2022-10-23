for x in range (10,100):
    for y in range(10,100):
        if int(str(x)+str(y)) == 11*(y+x):
            print(x,y)
