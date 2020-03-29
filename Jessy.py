def suma (a, b): 
    return a + b
def resta (a, b): 
    return a - b
def multiplicacion (a, b): 
    return a * b
def división (a, b): 
    return a / b
print("Escoga una operacion.") 
print("1.suma") 
print("2.resta") 
print("3.multiplicacion") 
print("4.Division")
opción = int(input())
a,b = int(input("introduzca número: ")),int(input("introduzca otro número: "))
if opción == 1:
    print(suma(a,b))
elif opción == 2:
    print(resta(a,b))
elif opción == 3:
    print(multiplicacion(a,b))
elif opción == 4:
    print(división(a,b))
else:
    print("opción invalida")