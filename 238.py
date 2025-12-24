class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = [1 for i in range(len(nums))]
        new_before = [1 for i in range(len(nums))]
        new_after = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            new_before[i] = new_before[i-1]*nums[i-1]
        
        for k in range(len(nums)-2,-1,-1):
            new_after[k] = new_after[k+1]*nums[k+1]
        for i in range(len(nums)):
            new[i] = new_before[i] * new_after[i]
        return new




