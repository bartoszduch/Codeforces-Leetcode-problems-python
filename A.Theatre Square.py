import math

print("wprowadz długosc placu")
m=int(input())
print("wprowadz szerokosc placu")
n=int(input())
print("wprowadz bok plyty")
a=int(input())


l1=math.ceil((m/a))
l2=math.ceil((n/a))

ilosc_plytek=l1*l2

print(ilosc_plytek)

print(math.ceil(3/2))