class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                b = int(stack.pop())
                a = int(stack.pop())
                if tokens[i] == '+':
                    output = a + b
                elif tokens[i] == '-':
                    output = a - b
                elif tokens[i] == '*':
                    output = a * b
                else:
                    output = int(a / b)
                stack.append(output)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]