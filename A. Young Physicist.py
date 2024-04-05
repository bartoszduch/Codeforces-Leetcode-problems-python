import math

t=int(input())
sumx=0
sumy=0
sumz=0

for i in range(t):
    a = list(map(int, input().split()))

    sumx+=a[0]
    sumy+=a[1]
    sumz+=a[2]
if sumx==0 and sumy==0 and sumz==0:
    print("YES")
else:
    print("NO")