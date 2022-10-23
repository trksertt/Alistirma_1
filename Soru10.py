liste=[]
for x in range(10000,100000):
    y=list(str(x))
    if y[0]==y[3] and y[1]==y[4]:
        liste.append(x)
print(len(liste))
