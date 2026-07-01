class Solution:
    def decodeString(self, s: str) -> str:
        count_stack=[]
        string_stack=[]

        curr=""
        num=0

        for char in s:
            if char.isdigit():
                num=num*10 + int(char) #INCASE ITS NOT ONE DIGIT LIKE 1,2 but its like 12 or 123
            
            elif char=="[":
                count_stack.append(num)
                string_stack.append(curr)
                curr=""
                num=0 #resetting curr n num for next use 
            
            elif char == "]":
                repeat = count_stack.pop()
                prev = string_stack.pop()
                curr = prev + curr * repeat

            else:
                curr += char

        return curr
            

        