class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        for i in range (len(numbers)):
            for j in range (len(numbers)):
                 if (i<j) and (i!=j):
                    if numbers[i]+numbers[j]==target:
                        ans.append(i+1)
                        ans.append(j+1)
        return ans 




        