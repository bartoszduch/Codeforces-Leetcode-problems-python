# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tab=[]
        point=head
        while point:
            tab.append(point.val)
            point=point.next
        
        n=len(tab)
        for i in range(n//2):
            if tab[i]==tab[-i-1]:
                continue
            else:
                return False
        return True
        
