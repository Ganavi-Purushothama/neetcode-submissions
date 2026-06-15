class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Number of valid subarrays found so far
        count = 0

        # Running total (prefix sum)
        prefix = 0

        # Dictionary storing:
        # prefix_sum : number of times we've seen it
        #
        # We start with {0:1}
        # because before reading any numbers,
        # our prefix sum is 0 once.
        seen = {0: 1}

        # Go through every number in the array
        for num in nums:

            # Add current number to running sum
            prefix += num

            # Ask:
            # "Have I seen a prefix sum equal to
            # (current prefix - k) before?"
            #
            # If yes, then a subarray summing to k exists.
            if prefix - k in seen:

                # Add however many times we've seen it
                count += seen[prefix - k]

            # Record current prefix sum in dictionary
            #
            # If prefix already exists,
            # increase its frequency by 1.
            #
            # Otherwise start it at 1.
            seen[prefix] = seen.get(prefix, 0) + 1

        # Return total number of valid subarrays
        return count