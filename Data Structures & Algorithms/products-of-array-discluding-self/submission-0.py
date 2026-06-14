class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[]
        for i in range (len(nums)):
            pro=1
            for j in range(len(nums)):
                if i!=j:
                    pro*=nums[j]
            p.append(pro)
        return p



            




        