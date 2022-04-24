from cgitb import text


numero=int(input("Ingrese un numero entre 0 y 999: "))

centena = int(numero / 100)
decena = int(numero % 100 / 10)
unidad = int(numero % 100 % 10)

texto = "Cetena =  {}".format(centena),"Decena = {}".format(decena),"Unidad = {}".format(unidad)

#print ("Centena =", centena)
#print ("Decena =", decena)
#print ("Unidad =", unidad)

print(texto)