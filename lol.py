print "1.Tovar 100 som"
print "2.Tovar 200 som"
print "3.Tovar 300 som"
tovar = str(input("> "))
if tovar == "1":
    print "Vvedite kolichestvo tovara"
    kolichestvo = int(input ("> "))
    summa = kolichestvo * 100
    print "Cena tovara %d" % summa 
    if summa < 500:
        print "Vvedite summu k oplate"
        oplata = int(input("> "))
        if oplata > summa:
            sdacha = oplata - summa
            print "Sdacha"
            print sdacha
        if oplata < summa:
            print "U vas ne hvataet sredstv, vvedite oplatu povtorno! "
        if oplata == summa:
            print "Spasibo"
    if summa > 500:
         print "Vvedite summu k oplate"
         print "Vasha skidka - 80 som"
         oplata = int(input("> "))
         skidka = summa - 80
         if oplata > summa:
            sdacha = oplata - skidka
            print "Sdacha"
            print sdacha
         if oplata < summa:
            print "U vas ne hvataet sredstv, vvedite oplatu povtorno! "
         if oplata == skidka:
            print "Spasibo"
  
