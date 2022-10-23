x=int(input("Lütfen bir sayı giriniz: "))

if x > 1:
    for i in range(2,x):
        if x%i==0:
            print(x,"asal bir sayı değildir.")
            break
    else:
        print(x,"asal bir sayıdır.")
else:
    print(x,"asal bir sayı değildir.")
