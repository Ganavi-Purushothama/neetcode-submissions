class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # Stack stores:
        # (starting_index, height)
        #
        # Example:
        # [(0,2), (2,5), (3,6)]
        #
        stack = []

        # Store the largest rectangle found so far
        maxArea = 0

        # Go through every bar
        for i, h in enumerate(heights):
            #enumerate() gives you both the index and the value at the same time.

            # Assume this bar starts at its own index
            start = i

            # ------------------------------------------
            # If current height is SMALLER than the
            # previous height...
            #
            # ...the taller bars can no longer continue.
            #
            # So calculate their areas.
            # ------------------------------------------
            while stack and stack[-1][1] > h: #stack[-1][1] = height of tht bar

                # Remove previous taller bar
                index, height = stack.pop()

                # Calculate rectangle
                #
                # height = popped height
                #
                # width =
                # current index - where that bar started
                #
                area = height * (i - index)

                # Update answer
                maxArea = max(maxArea, area)

                # VERY IMPORTANT
                #
                # Current smaller bar can actually start
                # where the taller bar started.
                #
                start = index

            # Push current bar
            #
            # Notice we DON'T push (i,h)
            #
            # We push (start,h)
            #
            stack.append((start, h))

        # ------------------------------------------
        # Some bars never got popped.
        #
        # That means they extend until
        # the END of the histogram.
        # ------------------------------------------
        while stack:

            index, height = stack.pop()

            area = height * (len(heights) - index)

            maxArea = max(maxArea, area)

        return maxArea