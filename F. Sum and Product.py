from collections import defaultdict
qq = 0
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    # Count the frequency of sums and products
    sum_counts = defaultdict(int)
    product_counts = defaultdict(int)

    for i in range(n):
        for j in range(i + 1, n):
            sum_counts[a[i] + a[j]] += 1
            product_counts[a[i] * a[j]] += 1

    results = []

    for _ in range(q):
        x, y = map(int, input().split())
        result = 0

        if x in sum_counts:
            result += sum_counts[x]

        if y in product_counts:
            result += product_counts[y]

        results.append(result // 2)

    print(*results)
