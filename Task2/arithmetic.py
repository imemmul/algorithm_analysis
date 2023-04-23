def eval_expression(exp):
    stack = []
    for char in exp:
        if char == '(':
            stack.append(char)
        elif char == ')':
            sub_expression = ''
            while stack[-1] != '(':
                sub_expression = stack.pop() + sub_expression
            stack.pop()
            stack.append(str(eval(sub_expression)))
        else:
            stack.append(char)
    final_expression = ''.join(stack)
    return eval(final_expression)

def arithmetic_max_value(expression):
    n = len(expression)  # number of operands in the expression
    #m = len(expression) - n # number of operators
    print(n)
    results = []
    for i in range(0, n + 1, 2):
        # print(f"i {i}")
        for j in range(i + 2, n + 2, 2):
            new_exp = expression[:i] + '(' + expression[i:]
            # print(new_exp)
            new_exp = new_exp[:j] + ')' + new_exp[j:]
            results.append(eval_expression(new_exp))
    return max(results)
    
            
    # m = [[0] * n for _ in range(n)]  # Initialize DP array to 0
    # for i in range(n):
    #     m[i][i] = int(expression[2*i])  # Base case: single operand
    # for s in range(1, n):  # Subexpression length
    #     for i in range(n-s):  # Starting index
    #         j = i + s  # Ending index
    #         for k in range(i, j):
    #             op = expression[2*k+1]
    #             if op == '+':
    #                 m[i][j] = max(m[i][j], m[i][k] + m[k+1][j])
    #             else:  # op == '*'
    #                 m[i][j] = max(m[i][j], m[i][k] * m[k+1][j])
    # return m[0][n-1]

s = input().strip()
print(arithmetic_max_value(s))
