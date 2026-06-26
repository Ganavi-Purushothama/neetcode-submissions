class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in range (len(operations)):

            if operations[i] not in ["+", "D", "C"]:
                stack.append(int(operations[i]))

            elif operations[i]=="+":
                x=stack[-1]
                y=stack[-2]
                stack.append(x+y)

            elif operations[i]=="C":
                stack.pop()

            elif operations[i]=="D":
                stack.append(stack[-1] * 2)

        return sum(stack)



        