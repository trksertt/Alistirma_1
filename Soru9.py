for x in range(1,1000):
    if (int(x/100))+((int(x/10))%10)+x%10<9:
        print(x,end=" ")
