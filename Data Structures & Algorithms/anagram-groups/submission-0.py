class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            sortedS=''.join(sorted(s)) #sorted(s)makes a list 
            if sortedS not in dic:
                dic[sortedS]=[]
            dic[sortedS].append(s) #so we need join to make it a word
        return list(dic.values())


        
        
