x=int(input("Lütfen 3 veya 4 basamaklı bir sayı giriniz: "))
if x < 100 or x > 9999:
    print("Yanlış bir sayı girdiniz, lütfen 4 veya 5 basamaklı bir sayı giriniz.")
else:
    if x == int(str(x)[::-1]):
        print(x,"palindromik bir sayıdır.")
    else:
        print(x,"palindromik bir sayı değildir.")
