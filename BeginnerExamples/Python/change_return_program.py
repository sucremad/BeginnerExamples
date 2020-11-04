from math import floor,ceil

tutar=float(input("Tutar:"))
ödenen=int(input("Ödenen para:"))
para_ustu=ödenen-tutar

kurus=(para_ustu-floor(para_ustu))
tam=int(para_ustu-kurus)


print("para üstü {} tl {} kuruştur.".format(tam,int(ceil(kurus*100))))

kurus=int(ceil(kurus*100))

quarter = 0
dimes = 0
nikel = 0
penny = 0


if kurus>=25:
    quarter=quarter+int(kurus/25)
    kurus=kurus%25

    if kurus>=10:
        dimes=dimes +int(kurus/10)
        kurus=kurus%10
        if kurus>=5:
            nikel=nikel+int(kurus/5)
            kurus=kurus%5
            if kurus>=1:
                penny=penny+int(kurus/1)

    elif kurus>=10:
        dimes=int(kurus/10)
        kurus=kurus%10
        if kurus>=5:
            nikel=int(kurus/5)
            kurus=kurus%5
            if kurus>=1:
                penny=int(kurus/1)

    elif kurus >= 5:
        nikel = int(kurus / 5)
        kurus = kurus % 5
        if kurus >= 1:
            penny = int(kurus / 1)

    else:
        if kurus >= 1:
            penny = int(kurus / 1)
print("cent: {} quarters {}  dimes {} nikels {} pennies".format(quarter,dimes,nikel,penny))

