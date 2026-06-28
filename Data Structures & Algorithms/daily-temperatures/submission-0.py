class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                #While there are still waiting days AND today is warmer than the last waiting day
                prev=stack.pop() #Remove that waiting day because we finally found its answer.
                result[prev]=i-prev #today index-waiting day index=days waited
            stack.append(i)
        return result
        