#zad 3 lista produktów spożywczych, wyświetl tylko te których wartość to sztuki
 
zakupy = {"Jajka": "sztuki",
      	"Mąka": "kilogramy",
      	"Mleko": "litry",
      	"Banany": "sztuki",
		"Avocado": "sztuki",
		"Woda": "litry"}
lista = [key for key,value in zakupy.items() if value == "sztuki"]
print(lista)