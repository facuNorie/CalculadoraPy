print("------------")
print("Calculadora")
print("------------\n\n")

numero = input("Como te llamas? : ")
print ("Hola", numero,"\n")
numero=0

print("*****************")
print("Menu de opciones")
print("*****************")



print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division Entera")
print("6. Exponente")
print("7. Modulo o resto\n")


numero = int(input("¿Que opcion eliges? : "))

if numero == 1 :
    numero=0
    numero = int(input("Elige el primer numero : "))
    numero += int(input("Elige el segundo numero : "))
    print("El resultado de la suma es ",numero)

elif numero == 2 :
    numero=0
    numero = int(input("Elige el primer numero : "))
    numero -= int(input("Elige el segundo numero : "))
    print("El resultado de la resta es ",numero)

elif numero == 3 :
    numero=0
    numero = int(input("Elige el primer numero : "))
    numero *= int(input("Elige el segundo numero : "))
    print("El resultado de la multiplicacion es ",numero)

elif numero == 4 :
    numero=0
    numero = int(input("Elige el primer numero : "))
    numero /= int(input("Elige el segundo numero : "))
    print("El resultado de la division es ",numero)

elif numero == 5 :
    numero=0
    numero = int(input("Elige el primer numero : "))
    numero //= int(input("Elige el segundo numero : "))
    print("El resultado de la division entera es ",numero)

elif numero == 6 :
    numero=0
    numero = int(input("Elige el primer numero : "))
    numero **= int(input("Elige el segundo numero : "))
    print("El resultado del exponente es ",numero)

elif numero == 7 :
    numero=0
    numero = int(input("Elige el primer numero : "))
    numero %= int(input("Elige el segundo numero : "))
    print("El resultado del modulo o resto es ",numero)






