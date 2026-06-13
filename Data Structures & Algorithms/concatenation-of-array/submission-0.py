class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans1=[]
        ans2=[]
        for num in nums:
            ans1.append(num)
            ans2.append(num)
        return ans1+ans2
        
