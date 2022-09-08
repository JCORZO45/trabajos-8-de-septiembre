
import math


print("----------------------")
print("---#programa de las llamadas:---")
print("----------------------")

#INPUT
b=input("Digite la duracion de la llamada : ")
b=int(b)

#PROCESAMIENTO
if b <= 3:
    #OUTPUT
    print("La llamada tiene un costo de: 300$")
else:
    d=((b-3)*50)+300
    #OUTPUT(2)
    print("La llamada tiene un costo de: "+str(d)+"$")
