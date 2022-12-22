"""
 В строке на вход три вида скобок {([])}. Надо проверить является ли строка
 валидной.

 Данный алгоритм имеет сложность O(n) - проходимся по всем элементам. O(n)
 памяти.
"""


def isValid(s):
    stack = []
    closeToOpen = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]: # стэк не пуской + нашли пару - выкидываем
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

s1 = "()[({}())"
s2 = "({[]}]"
s3 = "[](){}"
print(isValid(s1))
print(isValid(s2))
print(isValid(s3))