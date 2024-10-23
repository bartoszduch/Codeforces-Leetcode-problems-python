class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            total_ways = 0
            for i in range(n // 2 + 1):
                total_ways += self.neewton(n - i, i)
            return total_ways

    def neewton(self, a: int, b: int) -> int:
        return self.silnia(a) // (self.silnia(b) * self.silnia(a - b))

    def silnia(self, a: int) -> int:
        if a == 0:
            return 1
        wynik = 1
        for i in range(1, a + 1):
            wynik *= i
        return wynik
