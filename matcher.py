#Проверка скобок
#Первы йрабочий вариант
#----------------------
op_br = list("{[(<")
cl_br = list("}])>")
def check(st:list):
    for symbol in st:
        if not symbol in op_br:
            return False
    return True
st = input("Введите выражение для поиска: ")
ch_st = input("Введите скобки для поиска: ")
if not check(ch_st):
        print("Ошибка ввода! Допускается использовать только: {} варианты скобок".format(op_br))
        quit(1)
for br in ch_st:
    cl_br.append(cl_br[op_br.index(br)])
del cl_br[:4]
op_br = list(ch_st)
br_s = op_br + cl_br
st_ob = list()
for i in range(len(st)):
    if st[i] in br_s:
        if len(st_ob) == 0:
            if st[i] in op_br:
                st_ob.append((st[i], i))
            if st[i] in cl_br:
                print(False, (st[i]), None)
                quit()
        else:
            if st[i] in op_br:
                st_ob.append((st[i], i))
            if st[i] in cl_br:
                if st_ob[-1][0] == op_br[cl_br.index(st[i])]:
                    st_ob.pop()
                else:
                    print(False, (st[i], i), st_ob[-1])
                    quit()
if len(st_ob) != 0:
    print(False, None, st_ob[-1])
    quit()
print(True, None, None)