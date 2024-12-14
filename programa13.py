#Ingresar 10 valores por teclado y obtener la sumatoria de los mismos.
# Imprimir los resultados.


suma = 0
x = 0
while x < 10:
    valor = int(input("Ingrese un valor: "))
    suma += valor
    x += 1
print("La suma total es:", suma)
