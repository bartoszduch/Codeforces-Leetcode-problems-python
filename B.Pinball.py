import copy

def shift(string, a, n,shiftCount,ns):#n dlugosc znaku, a-indeks od ktorego zaczynamy
    if len(string)==1:
        return 1
    elif string[a] == '>':
        string[a] = '<'
        a += 1
        shiftCount+=1
        if a >=n:
            string[:]=ns
            return shiftCount
        else:
            return shift(string, a,n,shiftCount, ns)
    elif string[a] == '<':
        string[a] = '>'
        a -= 1
        shiftCount += 1
        if a<0:
            string[:]=ns
            return shiftCount
        else:
            return shift(string, a,n,shiftCount,ns)


t=int(input())
for i in range(t):
    n=int(input())
    s=list(input())
    ns = copy.deepcopy(s)
    for j in range(n):
        print(shift(s,j,n,0,ns),)