# stack O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val in ("+","-","*","/"):
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if val == "+":
                    stack.append(num1 + num2)
                elif val == "-":
                    stack.append(num1 - num2)
                elif val == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 / num2)

            else:
                stack.append(val)

        return int(stack.pop())