'''
Programa que convierta un valor dado en grados Fahrenheit
a grados Celsius
Entrada:
  temperatura en Fahrenheit: int->temperaturaF
  temperatura Celsius: int->temperaturaC

  Salida:
    Resultado de la temperatura


'''




print("inicio")
temperaturaF=int(input("ingrese la temperatura en grados Fahrenheit"))
temperaturaC=((temperaturaF-32)*5/9)
print("la temperatura en celsius es:", temperaturaC)