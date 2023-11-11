#dla 2 nie działa

x=int(input())

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a

def nww(a, b):
    return a * b // nwd(a, b)

for i in range(1,x//2):
    for j in range(1,x//2):
        if (nwd(i,j)+nww(i,j))==x:
            break

print("a:",i,"b:",j)