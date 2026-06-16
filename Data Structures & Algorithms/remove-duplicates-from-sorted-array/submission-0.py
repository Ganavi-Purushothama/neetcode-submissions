class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=[]
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen.append(nums[i])
        for j in range(len(seen)):
            nums[j]=seen[j]
        return len(seen)
            