class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Count how many of each character we NEED
        need = {}

        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        # Count characters in our CURRENT WINDOW
        window = {}

        left = 0

        # How many required characters have we satisfied?
        have = 0

        # Total unique characters we need
        needCount = len(need)

        # Store best answer
        res = ""
        resLen = float("inf")

        # Expand window
        for right in range(len(s)):

            c = s[right]

            # Add new character to window
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            # If this character is required
            # and we now have enough of it
            if c in need and window[c] == need[c]:
                have += 1

            # If window contains everything
            while have == needCount:

                # Update shortest answer
                if (right - left + 1) < resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1

                # Remove left character
                window[s[left]] -= 1

                # If removing it makes window invalid
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                # Shrink window
                left += 1

        return res

        