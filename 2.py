"""
На вход мат. выражение +-*/ + скобки. Вывод - результат выражения.
Пример: 2+7*(3/9)-5=
"""
import re

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def is_name(str):
    return re.match("\w+", str) # любая буква 1 или более


def peek(stack):
    return stack[-1] if stack else None # просмотр следующего элемента


def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval("{0}{1}{2}".format(left, operator, right)))


def greater_precedence(op1, op2):
    precedences = {'+': 0, '-': 0, '*': 1, '/': 1}
    return precedences[op1] > precedences[op2]


def evaluate(expression):
    if "=" in expression:
        expression.replace("=", "")
    tokens = re.findall("[+/*()-]|\d+", expression)
    values = []
    operators = []
    for token in tokens:
        if is_number(token):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop()  # избавиться от (
        else:
            # оператор
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)

    return values[0]

expression = '2+(3 * 6 + (5 - 3))+(8 - 2)='
print(format(evaluate(expression)))