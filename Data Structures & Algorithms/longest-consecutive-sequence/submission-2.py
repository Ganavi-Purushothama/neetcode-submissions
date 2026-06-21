class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        curr=1
        best=1

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i+1]==nums[i]+1:
                curr+=1
            else:
                best=max(best,curr) #here we copying the curr value to best n stoting, incase we have a larger better consecutive range cmg up
                curr=1 #remaking curr to 1 and assigning 
        best=max(best,curr)
        return best




    