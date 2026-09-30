class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # num_1 = int(tokens[0])

        stack = deque()

        for i in range(len(tokens)):
            match tokens[i]:
                case "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2+num1)
                case "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2-num1)
                case "*":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2*num1)
                case "/":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    num3 = num2/num1
                    if num3<0:
                        num3=math.ceil(num3)
                    else:
                        num3=math.floor(num3)
                    stack.append(num3)
                case _:
                    stack.append(int(tokens[i]))
           

        return stack.pop()
            

        