from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token not in operators:
                # The token is a number (operand)
                try:
                    # Append the integer value of the operand
                    stack.append(int(token)) 
                except ValueError:
                    # Handle cases where the token is not a valid integer/number
                    print(f"Error: Invalid token found: {token}")
                    return 0 # Or raise an exception
            else:
                # The token is an operator
                if len(stack) < 2:
                    # Should not happen with valid RPN input
                    print("Error: Not enough operands for operator.")
                    return 0
                    
                # 1. Pop the second operand (op2) - it was added last
                op2 = stack.pop() 
                # 2. Pop the first operand (op1) - it was added before op2
                op1 = stack.pop() 
                
                result = 0
                
                if token == '+':
                    result = op1 + op2
                elif token == '-':
                    result = op1 - op2
                elif token == '*':
                    result = op1 * op2
                elif token == '/':
                    # Python's default int division (//) truncates towards negative infinity.
                    # RPN often requires truncation towards zero (like in C/Java).
                    # int(op1 / op2) achieves truncation toward zero.
                    result = int(op1 / op2) 

                # 3. Push the result back onto the stack
                stack.append(result)
        
        # The final result is the single element left on the stack
        if len(stack) == 1:
            return stack[0]
        else:
            # Should not happen with valid RPN input
            print("Error: Invalid RPN expression - stack size is not 1 at the end.")
            return 0

# Optional: You can visualize the RPN evaluation process with a diagram.
#