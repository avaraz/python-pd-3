#zad 7 obliczanie przeciwprostokatnej z pitagorasa

import math as m
 
def przeciwprostokatna(a=4,b=3):
  c = m.sqrt(a**2 + b**2)
  return c
 
a,b = int(input("Podaj długość przyprostokątnych: ")), int(input())

print("Domyślna przeciwprostokątna:", przeciwprostokatna())
print(f"c^2 = {a}^2 + {b}^2")
print("Twoja przeciwprostokątna:", przeciwprostokatna(a,b))
