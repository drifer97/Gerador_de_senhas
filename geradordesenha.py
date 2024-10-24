import random


letras_maiuscula = chr(random.randint(65, 90))
letras_minuscula = chr(random.randint(97, 122))
char_especial = chr(64)
lista_numeros = []


for i in range(5): #ate 8 digitos

  numeros = random.randrange(9)

  lista_numeros.append(numeros)
  random.shuffle(lista_numeros)
lista_numeros = str(lista_numeros) [1:-1]
lista_numeros = lista_numeros.replace(',', '')

print(letras_maiuscula, letras_minuscula, lista_numeros, char_especial)