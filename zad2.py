#zad 2 Python comprehension Losowa macierz 4x4, wyświetl liczby po przekątnej

import numpy as np
 
macierz = np.random.randint(0,10, size=(4,4))
lista = [x for x in macierz.diagonal()]
print(macierz)
print("\n", lista)
