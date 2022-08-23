import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def arithmetic_arranger(problems, solved=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_row = ''
    second_row = ''
    lines = ''
    solutions = ''

    for problem in problems:
        num1 = problem.split()[0]
        operator = problem.split()[1]
        num2 = problem.split()[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        line_lenght = len(str(max(int(num1), int(num2)))) + 2
        line = line_lenght * '-'
        lines = lines + line + 4 * ' '
        first_row = first_row + num1.rjust(line_lenght, ' ') + 4 * ' '
        second_row = second_row + operator + num2.rjust(line_lenght - 1, ' ') + 4 * ' '

        solution = str(ops[operator](int(num1), int(num2)))
        solutions = solutions + solution.rjust(line_lenght, ' ') + 4 * ' '

    arranged_problems = first_row[:-4] + '\n' + second_row[:-4] + '\n' + lines[:-4]
    if not solved:
        return arranged_problems
    else:
        return arranged_problems + '\n' + solutions[:-4]
