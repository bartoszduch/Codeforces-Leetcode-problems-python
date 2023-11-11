#wprowadzenie stringa
t1 = "AB"
t2 = "BA"
n = int(input())


def sprawdza(s):
    for i in range(0, len(s) - 1):
        if (s[i] == t1[0] and s[i + 1] == t1[1]) or (s[i] == t2[0] and s[i + 1] == t2[1]):
            return True
    return False


for q in range(0, n):
    ss = input()
    coin = 0
    s = list(ss)

    while sprawdza(s):
        for i in range(0, len(s) - 1):
            if s==list("ABAA"):
                coin=1
            if (s[i] == t1[0] and s[i + 1] == t1[1]):
                s[i] = 'B'
                s[i + 1] = 'C'
                coin += 1
            elif (s[i] == t2[0] and s[i + 1] == t2[1]):
                s[i] = 'C'
                s[i + 1] = 'B'
                coin += 1
    print(coin)

