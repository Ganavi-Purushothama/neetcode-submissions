class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary search the SMALLER array.
        # This keeps the algorithm O(log(min(m,n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        # Binary search over all possible cut positions
        # in nums1.
        left = 0
        right = m

        while left <= right:

            # Where we cut nums1
            partitionX = (left + right) // 2

            # Total numbers needed on the LEFT side
            totalLeft = (m + n + 1) // 2

            # Whatever nums1 contributes,
            # nums2 contributes the rest.
            partitionY = totalLeft - partitionX

            # -----------------------------
            # Find the four boundary values
            #
            # leftX  | rightX
            # leftY  | rightY
            #
            # Example:
            #
            # nums1 = [1,3]
            #
            # 1 | 3
            #
            # leftX = 1
            # rightX = 3
            # -----------------------------

            # Largest value on left side of nums1
            if partitionX == 0:
                leftX = float("-inf")
            else:
                leftX = nums1[partitionX - 1]

            # Smallest value on right side of nums1
            if partitionX == m:
                rightX = float("inf")
            else:
                rightX = nums1[partitionX]

            # Largest value on left side of nums2
            if partitionY == 0:
                leftY = float("-inf")
            else:
                leftY = nums2[partitionY - 1]

            # Smallest value on right side of nums2
            if partitionY == n:
                rightY = float("inf")
            else:
                rightY = nums2[partitionY]

            # --------------------------------
            # Correct partition?
            #
            # Every left value must be <=
            # every right value.
            # --------------------------------
            if leftX <= rightY and leftY <= rightX:

                # Odd number of elements
                if (m + n) % 2 == 1:
                    return max(leftX, leftY)

                # Even number of elements
                return (max(leftX, leftY) + min(rightX, rightY)) / 2

            # --------------------------------
            # Took TOO MANY numbers from nums1.
            #
            # Move cut LEFT.
            # --------------------------------
            elif leftX > rightY:
                right = partitionX - 1

            # --------------------------------
            # Took TOO FEW numbers from nums1.
            #
            # Move cut RIGHT.
            # --------------------------------
            else:
                left = partitionX + 1