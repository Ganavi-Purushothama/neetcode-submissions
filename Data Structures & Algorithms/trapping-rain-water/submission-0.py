class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return  #empty array
        left=0
        right=len(height)-1

        leftMax=height[left]
        rightMax=height[right]
        water=0

        while left<right:
            if leftMax<rightMax:
                left+=1
                leftMax=max(leftMax,height[left])# Update tallest wall seen from left
                # Water trapped at current position
                #
                # Example:
                # leftMax = 5
                # current height = 2
                #
                # Water = 5 - 2 = 3
                water+=leftMax-height[left]
            else:
                right-=1
                rightMax=max(rightMax,height[right])
                water+=rightMax-height[right]
        return water
        