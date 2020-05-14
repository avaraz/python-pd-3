#zad 6 liczenie promienia z postaci kanonicznej
 
import math as m
 
def promien(a=2,b=-2,x=7,y=1):
  r2 = ((x-a)**2)-((y-b)**2)
  if r2 >= 0:
    r = m.sqrt(r2)
    return r
  else:
    r2 *= -1
    r = m.sqrt(r2)
    return r
 
print(promien())
