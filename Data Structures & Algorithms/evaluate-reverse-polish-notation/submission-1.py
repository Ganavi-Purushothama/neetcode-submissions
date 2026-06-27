class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))

            else:
                x = stack.pop()   # second operand
                y = stack.pop()   # first operand

                if token == "+":
                    stack.append(y + x)

                elif token == "-":
                    stack.append(y - x)

                elif token == "*":
                    stack.append(y * x)

                else:  # "/"
                    stack.append(int(y / x))  # truncate toward 0

        return stack[-1]