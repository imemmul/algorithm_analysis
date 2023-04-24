import sys

def eval(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b

def take_string(operand_1, operand_2, op, value):
    return str(operand_1) + op + str(operand_2) + "--->" + str(value)

def calculate(exp):
    length = len(exp)
    n = (length + 1) // 2 # number of operands
    # min_list = [tuple([[0] * n]) for i in range(n)] # creating min_list that keeps min evaluations
    # max_list = [tuple([[0] * n]) for i in range(n)] # creating max_list that keeps max evaluations
    min_list = [[0]*n for i in range(n)]
    max_list = [[0]*n for i in range(n)]
    # print(max_list)
    max_expression = []
    for i in range(n):
        # setting numbers to dioganol location
        min_list[i][i] = int(exp[2*i]) 
        max_list[i][i] = int(exp[2*i])
    # print(max_list)
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
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
                # TODO try to print expression that finds maximum value
                if max_val == a:
                    max_expression.append(take_string(min_list[i][k], min_list[k + 1][j], op, a))
                elif max_val == b:
                    max_expression.append(take_string(min_list[i][k], max_list[k + 1][j], op, b))
                elif max_val == c:
                    max_expression.append(take_string(max_list[i][k], min_list[k + 1][j], op, c))
                elif max_val == d:
                    max_expression.append(take_string(max_list[i][k], max_list[k + 1][j], op, d))
                else:
                    pass # max_value didn't change
            min_list[i][j] = min_val
            max_list[i][j] = max_val
    # print(max_expression)
    return max_list[0][n - 1]

if __name__ == "__main__":
    try:
        filename = sys.argv[-1]
        file = open(filename, "r")
        exp = file.readlines()
        print(calculate(exp[0]))
    except:
        print(f"Check your file name! \nUSAGE python arithmetic.py filename.txt")