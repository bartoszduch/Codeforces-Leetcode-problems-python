class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        numstr=str(num)
        czy_inne=False
        for char in numstr:
            if char!="0":
                czy_inne=True
        if not czy_inne:
            return True
        if numstr[-1]=="0" and czy_inne:
            return False
        return True

        
