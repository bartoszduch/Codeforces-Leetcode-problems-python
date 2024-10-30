class Solution:
    def trailingZeroes(self, n: int) -> int:
        power_of_5=5
        count=0
        while n>=power_of_5:
            count+=n//power_of_5
            power_of_5*=5
        return count