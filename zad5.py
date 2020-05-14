#zad 5 sprawdzanie czy dwie proste są prostopadłe lub równoległe
 
def sprawdz(a1,a2):
    if a1==a2:
        return("Funkcje są równoległe.")
    elif a1*a2==-1:
        return("Funkcje są prostopadłe.")
    else:
        return("Funkcje nie są ani równoległe, ani prostopadłe.")
 
a1 = int(input("Podaj a1: "))
b1 = int(input("Podaj b1: "))
a2 = int(input("Podaj a2: "))
b2 = int(input("Podaj b2: "))
 
print(f"y1 = {a1}x + {b1}")
print(f"y2 = {a2}x + {b2}")
print(sprawdz(a1,a2))
