print "1.Tovar 100 som"
print "2.Tovar 200 som"
print "3.Tovar 300 som"
tovar = raw_input("> ")
if tovar == "1":
	print "Vvedite kolichestvo tovara"
	kolichestvo = int(raw_input ("> "))
	summa = int (kolichestvo) * 100
	print "Cena tovara %d" % summa 
	if summa > 500:
		skidka = int (summa) - 80
		print "Vam predostavlyaetsya skidka. Summa k oplate %d som. " % skidka
		print "Vvedite summu k oplate"
		oplata = raw_input("> ")
		if int(oplata) < int(skidka):
			print "U vas ne hvataet sredstv, vvedite oplatu povtorno! "
			oplata = raw_input ("> ")
			print "Sposibo za pokupku! "

if tovar == "2":
    print "Vvedite kolichestvo tovara"
    kolichestvo = int(raw_input("> "))
    summa = int(kolichestvo) * 200
    print "Cena tovara %d" % summa
    if summa > 500:
    	skidka = int(summa) - 100 
    	print "Vam predostavlyaetsya skidka. Summa k oplate %d som. " % skidka 
    	print "Vvedite summu k oplate"	
    	oplata = raw_input("> ")
    	if int(oplata) < int(skidka):
    	    print "U vas ne hvataet sredstv, vvedite oplatu povtorno"
    	    oplata = raw_input ("> ")

if tovar == "3":
    print "Vvedite kolichestvo tovara"
    kolichestvo = int(raw_input("> "))
    summa = int(kolichestvo) * 300
    print "Cena tovara %d" % summa
    if summa > 500:
    	skidka = int(summa) - 150 
    	print "Vam predostavlyaetsya skidka. Summa k oplate %d som. " % skidka 
    	print "Vvedite summu k oplate"	
    	oplata = raw_input("> ")
    	if int(oplata) < int(skidka):
    	    print "U vas ne hvataet sredstv, vvedite oplatu povtorno"
    	    oplata = raw_input ("> ")
        
        

