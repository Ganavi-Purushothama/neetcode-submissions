from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()      # stores indices
        ans = []

        for i in range(len(nums)):

            # Remove indices outside the window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Remove all smaller elements from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Add current index
            q.append(i)

            # First complete window starts at i = k-1
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans