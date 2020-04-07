from random import random

macierz = [[random()  for i in range(4)] for i in range(4)]
print(macierz)

przekatna=[macierz[i][i] for i in range(len(macierz))]
print(przekatna)