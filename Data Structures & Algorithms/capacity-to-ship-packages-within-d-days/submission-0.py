class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        
        
        while(left<=right):
            mid=(left+right)//2

            days_use=1
            curr=0

             # Check if capacity = mid works
            for weight in weights:

                if curr + weight <= mid:
                    curr += weight

                else:
                    days_use += 1
                    curr = weight

            if days_use <= days:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans
