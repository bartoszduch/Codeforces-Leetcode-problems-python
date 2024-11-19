class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        posortowana=sorted(nums)
        print(posortowana)
        n=len(posortowana)
        left=0
        middle=1
        right=2
        sum=posortowana[0]+posortowana[1]+posortowana[2]
        while sum<target:
            if right>=n:
                return sum
                break
            sum=posortowana[left]+posortowana[middle]+posortowana[right]
            left+=1
            middle+=1
            right+=1
        return sum
