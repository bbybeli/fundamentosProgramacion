'''
programa que calcule el area y el perimero de un rectangulo a partir de su base y su altura 
Entradas:
   base:integer
   altura: integer
Salidas
   perimetro:integer
   area:interger
Analisis:
   Se requiere calcular con las formulas para area y perimetro
'''
# input siempre regresa un string
# para tratarlo como otro dato se debe convertir
base=input("Escribe la base del rectangulo:")
base= int(base)
altura=input("Escribe la altura del rectangulo:")
altura= int (altura)
area= base * altura
perimetro= base + base + altura +altura
print(area)
print(perimetro)
