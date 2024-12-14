#Realizar un algoritmo para determinar el sueldo de un empleado, teniendo en
# cuenta que si trabajo menos de 5 años la antigüedad será del 30% y si trabajo igual o
# más de 5 años del 50%. Sueldoacobrar=sueldo+(sueldo*%)


sueldo = int(input("Ingrese el sueldo del empleado: "))
años_trabajo = int(input("Ingrese los años trabajados: "))
if años_trabajo < 5:
    antiguedad = sueldo * 0.3
else:
    antiguedad = sueldo * 0.5
sueldo_total = sueldo + antiguedad
print("El sueldo a cobrar es:", sueldo_total)
