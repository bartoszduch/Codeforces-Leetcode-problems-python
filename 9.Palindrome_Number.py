class Solution:
    def isPalindrome(self, x: int) -> bool:
        list = str(x)
        list4 = []
        list2 = []
        for i in range(len(list)):
            list4.append(list[i])
            list2.append(list[-i - 1])
        if list2 == list4:
            return True
        else:
            return False

