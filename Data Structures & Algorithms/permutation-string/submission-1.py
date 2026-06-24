class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        # frequency of s1
        for c in s1:
            #count1[c] = count1.get(c, 0) + 1
            if c in count1:
                count1[c]+=1
            else:
                count1[c]=1

        # first window
        for i in range(len(s1)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        if count1 == count2:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            # add new character entering window
            count2[s2[right]] = count2.get(s2[right], 0) + 1

            # remove character leaving window
            count2[s2[left]] -= 1

            # clean up zero counts
            if count2[s2[left]] == 0:
                del count2[s2[left]]

            left += 1

            if count1 == count2:
                return True

        return False