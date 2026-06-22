class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()   
        left = 0        
        best = 0          

        for right in range(len(s)):  # expand window to the right

            # if duplicate found
            while s[right] in seen:

                # remove chars from left until duplicate disappears
                seen.remove(s[left])
                left += 1

            # add current character if not a duplicate
            seen.add(s[right])

            # current window length
            curr_len = right - left + 1

            # update answer
            best = max(best, curr_len)

        return best