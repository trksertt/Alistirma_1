liste=[]

for x in range(1000,10000):
    if int((x/1000))<(x%10):
        liste.append(x)
print(len(liste))
