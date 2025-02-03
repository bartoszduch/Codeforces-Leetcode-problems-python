class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum=max(nums)
        maximum2=-float(inf)
        maximum3=-float(inf)
        for i in range(len(nums)):
            if nums[i]>maximum2 and nums[i]<maximum:
                maximum2=nums[i]
        for i in range(len(nums)):
            if nums[i]>maximum3 and nums[i]<maximum2:
                maximum3=nums[i]
        if maximum3!=(-float(inf)):
            return maximum3
        return maximum

        
