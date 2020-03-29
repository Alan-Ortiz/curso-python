peso = int(input("Peso (Kg):"))
talla = float(input("talla (m):"))
imc = peso / talla**2
print("índice de Masa Corporal:",imc)

if imc < 18:
    print("Usted está en Desnutrición")
elif imc > 30:
    print("Usted está en Obesidad")
elif imc > 25 and imc < 30:
    print("Usted está en Sobrepeso")
else imc > 18 and imc < 25:
    print("Usted tiene Normopeso")