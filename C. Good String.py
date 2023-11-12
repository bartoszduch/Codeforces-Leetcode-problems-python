def make_left(string):
    n=len(string)
    first=string[0]
    nowy=[None]*n
    for i in range(0,n-1):
        nowy[i]=string[i+1]
    nowy[n-1]=first
    return nowy

def make_right(string):
    n=len(string)
    last=string[n-1]
    nowy=[None]*n
    for i in range(0,n-1):
        nowy[i+1]=string[i]
    nowy[0]=last
    return nowy


def if_rnl(string):
    if make_left(string)==make_right(string):
        return True
    else:
        return False






#test=int(input)
#for i in range (0,test):
