#zad 4 monotoniczność funkcji liniowej

def montonicznosc(a,b):
    if a>0:
        print(f"y = {a}x + {b}")
        return("Funkcja jest rosnąca.")
    elif a<0:
	    print(f"y = {a}x + {b}")
	    return("Funkcja jest malejąca.")
    else:
	    print(f"y = {b}")
	    return("Funkcja jest stała.")
 
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
 
print(montonicznosc(a,b))
