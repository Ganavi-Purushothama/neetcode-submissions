class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        ans=right

        while(left<=right):
            mid=(left+right)//2
            pieces=1
            curr=0

            for num in nums:
                if curr + num > mid:
                    pieces+=1
                    curr=num 

                else:
                    curr+=num
            
            if pieces <= k:
                ans = mid

                # Try making maximum even smaller
                right = mid - 1

            else:

                # Need a larger maximum sum
                left = mid + 1



        
        return ans