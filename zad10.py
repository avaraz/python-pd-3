#zad 10 funkcja wykorzystuje **, wczytuje listę zakupów i wyświetla sume ich wartosci
 
def zakupy(** produkty):
    if len(produkty) == 0:
        return 0
    else:
        suma = 0
        for ilosc in produkty.values():
            suma += ilosc
        return suma
 
print(zakupy())
print(zakupy(jajka=12, jablka=3, chleb=5, maslo=4))