class Solution:
    def reverseWords(self, s: str) -> str:
        slowa=s.split()
        slowa.reverse()
        wynik=" ".join(slowa)
        return wynik
