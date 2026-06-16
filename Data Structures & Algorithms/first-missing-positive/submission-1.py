class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        want=1
        for i in range(len(nums)):
            if nums[i]==want:
                want+=1
            elif nums[i]<want:
                continue
            else:
                return want
        return want


                    
                    
                    
        