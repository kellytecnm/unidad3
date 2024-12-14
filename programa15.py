#Ingresar 100 valores por teclado y determinar cuántas veces el valor ingresado
# es: a) Mayor a 0 y menor a 10
# b) Esta comprendido entre 10 y 100 ambos inclusive.
# c) Es mayor a 100
# d) Es negativo
# e) Es igual a 0 Imprimir los resultados.


cont_menora10 = 0
cont_10a100 = 0
cont_mayorque100 = 0
cont_negativo = 0
cont_cero = 0

for cont in range(100):
    valor = int(input("Ingrese un valor: "))
    if 0 < valor < 10:
        cont_menora10 += 1
    elif 10 <= valor <= 100:
        cont_10a100 += 1
    elif valor > 100:
        cont_mayorque100 += 1
    elif valor < 0:
        cont_negativo += 1
    else:
        cont_cero += 1

print("Mayor a 0 y menor a 10:", cont_menora10)
print("Entre 10 y 100:", cont_10a100)
print("Mayor a 100:", cont_mayorque100)
print("Negativo:", cont_negativo)
print("Igual a 0:", cont_cero)
