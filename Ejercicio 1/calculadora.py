import math

def suma(x, y):
    return x + y
def resta(x,y):
    return x - y
def multi(x, y):
    return x * y
def division(x, y):
    return x / y
def raiz(x):
    return math.sqrt(x)

print("1 suma")
print("2 resta")
print("3 multiplicacion")
print("4 division")
print("5 raiz cuadrada")

opcion= int(input("cual operacion desea?"))


if opcion == 1:
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("El resultado es:", suma(num1, num2))
elif opcion == 2:
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("El resultado es:", resta(num1, num2))
elif opcion == 3:
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("El resultado es:", multi(num1, num2))
elif opcion == 4:
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("El resultado es:", division(num1, num2))
elif opcion == 5:
    
    num1 = float(input("Ingrese el número: "))
    print("El resultado es:", raiz(num1))