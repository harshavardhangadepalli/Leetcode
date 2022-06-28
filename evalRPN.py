class Solution:
    def evalRPN(self, tokens):
        stack = list()
        for item in tokens:
            if item == '+':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(int(op1+op2))
            elif item == '-':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(int(op1-op2))
            elif item == '*':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(int(op1*op2))
            elif item == '/':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(int(op1/op2))
            else:
                stack.append(int(item))
        return stack.pop()

s = Solution()
print(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))