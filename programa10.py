#en un curso de computación, que consta de 24 alumnos, deberán armar un
# algoritmo que informe por pantalla el apellido y nombre junto a la nota de
# examen de cada alumno.


a = 0
while a < 24:
    apellido = input("Ingrese el apellido del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    nota = int(input("Ingrese la nota del examen: "))
    print(f"{apellido} {nombre} - Nota: {nota}")
    a += 1
