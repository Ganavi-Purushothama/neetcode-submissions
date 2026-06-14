class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs: #["Hello","World"]
            res+=str(len(s)) + "#" + s #'5#Hello5#World'
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            hash_pos=i
            while s[hash_pos]!="#": #  describes the end of a word w its length 
                hash_pos+=1
            length_w=int(s[i:hash_pos]) #find the length of the word 

            word = s[hash_pos+1 : hash_pos+1+length_w] #"5#Hello5#"

            res.append(word)

            i=hash_pos+1+length_w
        return res


        

