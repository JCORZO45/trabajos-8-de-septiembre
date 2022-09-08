
import math


print("----------------------")
print("---#determine si sus dos últimos dígitos son iguales:---")
print("----------------------")

#INPUT
b=input("Digite un numero entero  : ")
b=int(b)

#PROCESAMIENTO
d1=b%10
a2= ((b%100)-d1)//10
S=d1+a2

if S>=10:
    print("El resultado es de 2 digitos")
else:
    print("El resultado es de 1 digitos")
