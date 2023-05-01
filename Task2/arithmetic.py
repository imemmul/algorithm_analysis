import sys

def eval(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b

# def take_string(operand_1, operand_2, op, value):
#     return str(operand_1) + op + str(operand_2) + "--->" + str(value)

import sys

import sys

def calculate(exp):
    length = len(exp)
    n = (length + 1) // 2 # number of operands
    # min_list = [tuple([[0] * n]) for i in range(n)] # creating min_list that keeps min evaluations
    # max_list = [tuple([[0] * n]) for i in range(n)] # creating max_list that keeps max evaluations
    min_list = [[0]*n for i in range(n)]
    max_list = [[0]*n for i in range(n)]
    for i in range(n):
        # setting numbers to diagonal location
        min_list[i][i] = int(exp[2*i]) 
        max_list[i][i] = int(exp[2*i])
    max_expression = [["" for _ in range(n)] for _ in range(n)]
    for i in range(n):
        max_expression[i][i] = str(exp[2*i])
    for s in range(n - 1):
        for i in range(n - s - 1):
            j = i + s + 1
            min_val = sys.maxsize
            max_val = -sys.maxsize
            # find the minimum and maximum values for the expression
            # between the ith number and jth number as Emre hoca said in 04/24
            for k in range(i, j):
                # below calculating every possible of pairs which 2^2 = 4 for max and min value pairs
                op = exp[2 * k + 1]
                a = eval(min_list[i][k], min_list[k + 1][j], op)
                b = eval(min_list[i][k], max_list[k + 1][j], op)
                c = eval(max_list[i][k], min_list[k + 1][j], op)
                d = eval(max_list[i][k], max_list[k + 1][j], op)
                # TODO try to print expression that finds maximum value
                temp_max = max_val
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
                if max_val != temp_max: # if there is a change in max_value add to max_exression
                    max_expression[i][j] += f"({max_expression[i][k]}{op}{max_expression[k+1][j]})"
            min_list[i][j] = min_val
            max_list[i][j] = max_val
    return max_list[0][n - 1], max_expression[0][n - 1]

if __name__ == "__main__":
    try:
        filename = sys.argv[-1]
        file = open(filename, "r")
        exp = file.readlines()
        value, max_exp = calculate(exp[0])
        print(f"maximum-value: {value}")
        print("-" * 50)
        print(f"maximum expression that finds the value: {max_exp}")
    except:
        print(f"Check your file name! \nUSAGE python arithmetic.py filename.txt or there is another problem with code!!")