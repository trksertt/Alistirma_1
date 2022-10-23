for x in range(10000,100000):
    if x > 1:
        for i in range(2,x):
            if (x%i==0):
                break
        else:
            print(x)
