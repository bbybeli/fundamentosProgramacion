'''
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
 las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
 en cuenta su sueldo base y comisiones.

Entrada:
sueldo_base:float
venta1,venta2,venta3:float
Salida:
   el sueldo_base mas su comision
 

'''


sueldo_base = float(input("Dime el sueldo base:"))
venta1 = float(input("Dime precio de la venta 1:"))
venta2 = float(input("Dime precio de la venta 2:"))
venta3 = float(input("Dime precio de la venta 3:"))
comision = venta1 * 0.10+ venta2 * 0.10 + venta3 * 0.10
print("Comisión por ventas:",comision)
print("Sueldo total:", sueldo_base + comision)