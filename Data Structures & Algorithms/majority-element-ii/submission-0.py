class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        seen=[]
        for i in range(len(nums)):
            key=nums[i]
            if key in seen:
                continue
            seen.append(key)
            count=0
            for j in range(len(nums)):
                if nums[j]==key:
                    count+=1
                else:
                    continue 
            if (count>(len(nums)/3)):
                ans.append(key)
        return ans

                





        