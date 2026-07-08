class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # Found the target
            if nums[mid] == target:
                return mid

            # -------------------------------------------------
            # Check if the LEFT half is sorted
            #
            # Example:
            # [4,5,6,7 | 0,1,2]
            #  L     M
            #
            # Since 4 <= 7, the left half is sorted.
            # -------------------------------------------------
            if nums[left] <= nums[mid]:

                # Is the target inside the sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # Otherwise search the right half
                    left = mid + 1

            # -------------------------------------------------
            # Otherwise, the RIGHT half must be sorted
            #
            # Example:
            # [6,7 | 0,1,2,3]
            #       M       R
            # -------------------------------------------------
            else:

                # Is the target inside the sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # Otherwise search the left half
                    right = mid - 1

        # Target not found
        return -1
        