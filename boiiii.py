#!/usr/bin/env python

print("Hello World!")

tekst = "Hello World!"
tekst = 'Hello World!'
tekst = """Hello
 World!"""

print(type(tekst))
print(tekst)

print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)
print(5 // 5) #dzielenie bez reszty
print(5 % 5) #modulo
print(5 ** 5) #potega

print('Ala' + ' ma kota') #konkatynacja
print('Ala' + ' ma '+ str(5) + ' kota') 
liczba = int("250")
print('Ala '*10)

#listy
lista = []
print(type(lista))
lista2 = [1,2,3]
print(lista2[0])
imie = "Magdalena"
print(imie[0])
lista2[0] = 5
# imie[0] = "K" błąd
imie = imie.swapcase()
print(imie)
"Ala".swapcase()
lista3 = [1,'Ala', 4.5, None, True, [1,2]]
lista3[5][1] #Tu wstawić żart o Incepcji

macierz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
macierz[1][1]
nowa = lista2 + macierz

#słownik
slownik = {}
slownik['imie'] = 'Adam'
slownik[0] = 'Adam'
print(slownik)

slownik2 = {'imie':'Adam', 0:'Adam'}
print(slownik2.keys())
print(slownik2.values())

def pow():
    pass


    for element in kolekcja:

    from math import *
    import math as m
    from math import pow, sin, sqrt

m.pow()
m.pi

