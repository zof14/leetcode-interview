class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = 0
        curr_end=0
        jump=0
        i=0
        if len(nums)<=1:
            return 0
        for i in range(len(nums)-1):
            curr = max(curr,nums[i]+i)
            if i == curr_end:
                jump+=1
                curr_end = curr

                if curr_end>= len(nums)-1:
                    break
        return jump
       


        