class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        max_f=0
        left=0
        best=0

        for right in range(len(s)):
            #count[s[right]]= count.get(s[right],0)+1
            #means exactly as the below if-else statement
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            max_f=max(max_f,count[s[right]])

            #replacement need = window_size-highest_freq 
            while(right-left+1)-max_f>k:
                count[s[left]]-=1 #remove left char
                left+=1 #shring the window

            best=max(best,(right-left+1))
        return best 

        