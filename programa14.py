#Ingresar 10 valores numéricos por teclado y calcular la suma, el promedio e
# imprimir la suma, el promedio agregando una leyenda en cada caso.

suma = 0
x = 0
while x < 10:
    valor = int(input("Ingrese un valor: "))
    suma += valor
    x += 1
promedio = suma / 10
print("La suma es:", suma)
print("El promedio es:", promedio)
