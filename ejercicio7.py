''' programa que reciba una cantidad de minutos y muestre por pantalla a 
cuantas horas y minutos corresponde

Entrada:
Los minutos=int->minutos
 Las horas=int->res_horas 
 Los minutos=int-> res_min
Salida:
Resultado de horas y minutos
'''
minutos = int(input("Introduce la cantidad de minutos:"))
res_horas = minutos // 60
res_min = minutos % 60
print(res_horas,"horas y",res_min,"minutos.")