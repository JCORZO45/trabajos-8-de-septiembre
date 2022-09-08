
import math


print("----------------------")
print("---#determine si sus dos últimos dígitos son iguales:---")
print("----------------------")

#INPUT
b=input("Digite un numero entero  : ")
b=int(b)

#PROCESAMIENTO
c=b%10
d= ((b%100)-c)//10

if c==d:
    print("Sus dos últimos dígitos son iguales")
else:
    print("Sus dos últimos dígitos NO son iguales")



