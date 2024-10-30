import time


def Hanoi(n, A, B, C):
    if n==1:
        print(A,"->",B)
    else:
        Hanoi(n-1,A,C,B)
        print(A,"->",B)
        Hanoi(n-1,C,B,A)


def possible_move(source, target, source_name, target_name):
    if not source:
        disk = target.pop()
        source.append(disk)
        print(f"Przenieś krążek {disk} z {target_name} do {source_name}")
    elif not target:
        disk = source.pop()
        target.append(disk)
        print(f"Przenieś krążek {disk} z {source_name} do {target_name}")
    elif source[-1] < target[-1]:
        disk = source.pop()
        target.append(disk)
        print(f"Przenieś krążek {disk} z {source_name} do {target_name}")
    else:
        disk = target.pop()
        source.append(disk)
        print(f"Przenieś krążek {disk} z {target_name} do {source_name}")


def hanoi_iterative(n):
    sour = list(range(n, 0, -1))
    dest = []
    buff = []

    sour_name, dest_name, buff_name = "A", "B", "C"

    total_moves = 2 ** n - 1

    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            possible_move(sour, dest, sour_name, dest_name)
        elif i % 3 == 2:
            possible_move(sour, buff, sour_name, buff_name)
        elif i % 3 == 0:
            possible_move(buff, dest, buff_name, dest_name)

hanoi_iterative(3)

star=time.time()
Hanoi(10,"A","B","C")
stop=time.time()

stari=time.time()
hanoi_iterative(20)
stopi=time.time()

print("czas rekur to: ", stop-star)
print("czas iteracyjny to: ", stopi-stari)