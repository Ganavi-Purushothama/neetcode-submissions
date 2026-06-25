class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        best=float("inf")
        curr_sum=0

        for right in range (len(nums)):
            curr_sum+=nums[right]

            while curr_sum>=target:
                best=min(best,right-left+1)
                #shrink window 
                curr_sum-=nums[left]
                left+=1
        if best == float("inf"):
            return 0

        return best


