def check(str,brackets_open = ('(','[','{','<')):
    brackets_closed = (')',']','}','>')
#    brackets_closed = []
#       for j in brackets_open:
#        if brackets_open.index(j) == '(':
#            brackets_closed = ')'
#        elif brackets_open.index(j) == '{':
#            brackets_closed = '}'
#        elif brackets_open.index(j) == '[':
#            brackets_closed = ']'
#        elif brackets_open.index(j) == '<':
#            brackets_closed = '>'
#        else:
#            return ("Не верный синтаксис")
    stack = []
    for i in str:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else: return False
    return (not stack)
st = input("Введите строку:")
#br = (input("Введите скобки"))
a = check(st)
print(a)