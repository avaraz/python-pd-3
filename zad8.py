#zad 8 suma dowolnego ciągu arytmetycznego
 
def ciag(a1=1, r=1, ile=10):
  suma = ((2*a1+(ile-1)*r)/2)*ile
  return suma
 
a1 = int(input("Podaj pierwszy wyraz ciągu: "))
r = int(input("Podaj o ile ciąg ma się zwiększać: "))
ile = int(input("Podaj ile elementów ciągu ma sumować: "))
print("Suma domyślnego ciągu: ", ciag())
print("Suma dowolnego ciągu: ", ciag(a1,r,ile))
