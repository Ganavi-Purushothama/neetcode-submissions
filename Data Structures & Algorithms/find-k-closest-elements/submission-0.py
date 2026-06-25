class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        # Remove the farthest elements until only k remain
        while right - left + 1 > k:

            # If left element is farther from x, remove it
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1

            # Otherwise remove the right element
            else:
                right -= 1

        return arr[left:right + 1]