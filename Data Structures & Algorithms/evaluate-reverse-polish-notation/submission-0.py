class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack = []
        for token in tokens:
            if token == "+":
                eval_stack.append(int(eval_stack[-2]) + int(eval_stack[-1]))
                eval_stack.pop(-2)
                eval_stack.pop(-2)
            elif token == "-":
                eval_stack.append(int(eval_stack[-2]) - int(eval_stack[-1]))
                eval_stack.pop(-2)
                eval_stack.pop(-2)
            elif token == "*":
                eval_stack.append(int(eval_stack[-2]) * int(eval_stack[-1]))
                eval_stack.pop(-2)
                eval_stack.pop(-2)
            elif token == "/":
                eval_stack.append(int(int(eval_stack[-2]) / int(eval_stack[-1])))
                eval_stack.pop(-2)
                eval_stack.pop(-2)
            else:
                eval_stack.append(int(token))
        return eval_stack[0]