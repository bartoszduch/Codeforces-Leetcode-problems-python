import math

def find_beautiful_coloring(n, a):
    gcd = a[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, a[i])

    if gcd == 1:
        return 0  # No beautiful coloring is possible if GCD is 1.

    return gcd

# Input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Find a beautiful coloring value of d
    result = find_beautiful_coloring(n, a)
    print(result)