class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        small_w = strs[0]
        ans = ""

        # Find shortest string
        for s in strs:
            if len(s) < len(small_w):
                small_w = s

        # Check each position
        for i in range(len(small_w)):

            for s in strs:

                if s[i] != small_w[i]:
                    return ans

            ans += small_w[i]

        return ans
                
        









