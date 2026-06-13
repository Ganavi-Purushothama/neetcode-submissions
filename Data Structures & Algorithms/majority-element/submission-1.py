class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            key= nums[i] 
            count=0
            for j in range (len(nums)):
                if key == nums[j]:
                    count+=1

                if count>((len(nums))//2):
                    return key

            


