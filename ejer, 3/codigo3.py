import math


print("----------------------")
print("---#Determine si es un número positivo de 4 dígitos:---")
print("----------------------")

#INPUT
b=input("Digite un numero entero  : ")
b=int(b)

#PROCESAMIENTO
b=b//1000
if 10>b>0:

    print("El numeroo de 4 digitos")
else:
    print("El numero no es de 4 digitos")

    
