class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            alive=True 
            while alive and stack and stack[-1]>0 and a<0: #only enters loop if a is -ve and stack[-1] is +ve
                if abs(stack[-1])<abs(a):
                    stack.pop()
                elif abs(stack[-1])==abs(a):
                    stack.pop()
                    alive=False
                else:
                    alive=False
            if alive:
                stack.append(a)
        return stack


        