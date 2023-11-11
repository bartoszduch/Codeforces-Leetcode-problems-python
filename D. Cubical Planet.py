
w1=input()
w2=input()

m1 = [int(x) for x in w1.split()]
m2 = [int(x) for x in w2.split()]
if(m1[0]==m2[0]or m1[1]==m2[1] or m1[2]==m2[2]):
    print("yes")
else:
    print("no")