#zad 1 Zdefinuj zbiory przy użyciu Python comprehension

a = [1/x for x in range(1,11)]
print("A = ", a)
b = [2**x for x in range(11)]
print("B =", b)
c = [x for x in b if x%4 == 0]
print("C =", c)
