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
            # enumerate() gives both index and value.

            # Assume this bar starts at its own index
            start = i

            # If current height is smaller,
            # previous taller bars cannot continue.
            while stack and stack[-1][1] > h:

                # Remove previous taller bar
                index, height = stack.pop()

                # Rectangle formed by that taller bar
                area = height * (i - index)

                # Update answer
                maxArea = max(maxArea, area)

                # -----------------------------------------
                # VERY IMPORTANT!!
                #
                # The current bar is SHORTER.
                #
                # Every bar we just popped was TALLER,
                # so this shorter bar can also start
                # where those taller bars started.
                #
                # Example:
                #
                # Heights:
                #
                # 5 4
                #
                # Height 4 can use BOTH columns because
                # 5 >= 4.
                #
                # So instead of starting at index 1,
                # it actually starts at index 0.
                #
                # We "steal" the popped bar's start.
                # -----------------------------------------
                start = index

            # Push current bar.
            #
            # Notice we DON'T push (i, h)
            #
            # We push (start, h)
            #
            stack.append((start, h))

        # Bars left in the stack extend
        # all the way to the end.
        while stack:

            index, height = stack.pop()

            area = height * (len(heights) - index)

            maxArea = max(maxArea, area)

        return maxArea