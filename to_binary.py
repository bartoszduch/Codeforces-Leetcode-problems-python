a = bin(10)#funkcja pythona zamieniająca na binarne
def to_binary(n):
    number = []
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    while n > 0:
        number.append(n%2)
        n=n // 2
    number.reverse()
    return number


print(to_binary(10))

