class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr=0
        prev=0
        for i in range(len(nums)):
            if curr<0:
                return False
            elif nums[i]>curr:
                curr=nums[i]
            curr-=1
        return True