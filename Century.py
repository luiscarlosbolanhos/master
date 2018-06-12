number = input( "Ingrese una fecha: " )
if number%100 == 0 :
    print "Siglo " + str(number/100) 
else  :
    print "Siglo " + str((number/100)+1)
