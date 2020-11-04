#A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

from math import acos,asin,radians,atan,ceil,cos,degrees,exp,fabs,factorial,floor,sin,sqrt,tan,gamma,log10



print("MENU\n")
print("------------")
print("""1.Return the arc cosine (measured in radians) of x
2.Return the arc sine (measured in radians) of x.
3.Return the arc tangent (measured in radians) of x.
4.Return the ceiling of x as an Integral.(This is the smallest integer >= x.)
5.Return the cosine of x (measured in radians).
6.Convert angle x from radians to degrees
7.Return e raised to the power of x.
8.Return the absolute value of the float x.
9.Find x!.
10.Return the floor of x as an Integral.
11.Return the sine of x (measured in radians).
12.Return the square root of x.
13.Return the tangent of x (measured in radians).
14.Gamma function at x.
15.Return the base 10 logarithm of x.
16.Convert angle x from degrees to radians.
17.quit

UYARI!!:Tanım kümelerine uygun yazılmazsa hata verir.
""")



while True:
    sonuc=0
    islem=int(input("İşlem seçin:"))

    if islem==1:
        giris=float(input("Sayı:"))

        sonuc=acos(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==2:
        giris=float(input("Sayı:"))

        sonuc=asin(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==3:
        giris=float(input("Sayı:"))

        sonuc=atan(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==4:
        giris=float(input("Sayı:"))

        sonuc=ceil(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==5:
        giris=float(input("Sayı:"))

        sonuc=cos(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==6:
        giris=float(input("Sayı:"))

        sonuc=degrees(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem ==7:
        giris=float(input("Sayı:"))

        sonuc=exp(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==8:
        giris=float(input("Sayı:"))

        sonuc=fabs(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem ==9:
        giris=float(input("Sayı:"))

        sonuc=factorial(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==10:
        giris=float(input("Sayı:"))

        sonuc=floor(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==11:
        giris=float(input("Sayı:"))

        sonuc=sin(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==12:
        giris=float(input("Sayı:"))

        sonuc=sqrt(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem ==13:
        giris=float(input("Sayı:"))

        sonuc=tan(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem ==14:
        giris=float(input("Sayı:"))

        sonuc=gamma(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem ==15:
        giris=float(input("Sayı:"))

        sonuc=log10(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==16:
        giris=float(input("Sayı:"))

        sonuc=radians(giris)
        print("Sonuç: {}".format(sonuc))

    elif islem==17:
        break










