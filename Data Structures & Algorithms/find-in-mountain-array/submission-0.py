# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation.
#
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:
# """

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        n = mountainArr.length()

        # ---------------------------------
        # STEP 1: Find the peak
        # ---------------------------------
        left = 0
        right = n - 1

        while left < right:

            mid = (left + right) // 2

            # Still climbing up
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1

            # Going downhill
            else:
                right = mid

        peak = left

        # ---------------------------------
        # STEP 2: Binary Search (Ascending)
        # ---------------------------------
        left = 0
        right = peak

        while left <= right:

            mid = (left + right) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        # ---------------------------------
        # STEP 3: Binary Search (Descending)
        # ---------------------------------
        left = peak + 1
        right = n - 1

        while left <= right:

            mid = (left + right) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid

            # DESCENDING order
            elif value < target:
                right = mid - 1

            else:
                left = mid + 1

        return -1