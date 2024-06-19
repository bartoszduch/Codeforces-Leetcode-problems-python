l=int(str(11110),2)
print(l)
def to_decimal(n):
    n=str(n)
    decimal=0
    for i in range(len(n)):
        if n[-i-1]=="1":
            decimal+=2**i
    return decimal
print(to_decimal(110111011))

