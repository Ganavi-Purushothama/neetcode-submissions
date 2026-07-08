class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Binary search pointers
        left = 0
        right = len(nums) - 1

        # Keep shrinking the search space
        # until only ONE element is left.
        while left < right:

            mid = (left + right) // 2

            # -----------------------------------------
            # Compare middle with the LAST element.
            #
            # Why the last element?
            #
            # The last element tells us which side
            # of the rotation we're currently in.
            #
            # Example:
            #
            # [4,5,6,7,0,1,2]
            #            ^
            #          right = 2
            #
            # If nums[mid] > nums[right],
            # mid is in the LEFT sorted half.
            #
            # So the minimum must be AFTER mid.
            # -----------------------------------------
            if nums[mid] > nums[right]:

                # Throw away everything up to mid
                # because none of them can be minimum.
                left = mid + 1

            else:
                # -------------------------------------
                # nums[mid] <= nums[right]
                #
                # This means mid is in the RIGHT half,
                # where the minimum exists.
                #
                # IMPORTANT:
                # mid itself could actually BE
                # the minimum.
                #
                # Example:
                #
                # [5,6,1,2,3]
                #      ^
                #     mid
                #
                # If we did right = mid - 1,
                # we'd throw away the answer!
                #
                # So we KEEP mid.
                # -------------------------------------
                right = mid

        # -----------------------------------------
        # Loop stops when left == right.
        #
        # Both pointers are pointing at the
        # smallest element.
        #
        # Example:
        #
        # left
        #   ↓
        # [4,5,6,7,0,1,2]
        #          ↑
        #        right
        # -----------------------------------------
        return nums[left]