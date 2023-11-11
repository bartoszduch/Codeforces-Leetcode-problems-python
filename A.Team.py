n = 3
tab = [[1, 0, 0], [1, 1, 1], [1, 1, 0]]
counter = 0

for j in range(n):
    if (tab[j][0] == 1 and tab[j][1] == 1) or (tab[j][0] == 1 and tab[j][2] == 1) or (tab[j][1] == 1 and tab[j][2] == 1):
        counter += 1

print(counter)