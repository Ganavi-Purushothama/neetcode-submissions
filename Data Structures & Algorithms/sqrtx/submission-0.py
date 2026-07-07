class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        ans=0

        while left<=right:
            mid=(left+right)//2
            square=mid*mid

            if square == x:
                return mid

            elif square < x:
                ans = mid          # Best answer so far
                left = mid + 1     # Try a bigger number

            else:
                right = mid - 1    # Too big
        return ans

        