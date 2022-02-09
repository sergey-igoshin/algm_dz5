"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""

from timeit import timeit
from collections import deque

lst = [x for x in range(100)]
deq = deque(lst)


def lst_append():
    a = True
    return lst.append(a)


def deq_append():
    a = True
    return deq.append(a)


def lst_pop():
    return lst.pop()


def deq_pop():
    return deq.pop()


def lst_extend():
    a = [True, 1, 'text']
    return lst.extend(a)


def deq_extend():
    a = [True, 1, 'text']
    return deq.extend(a)


def lst_appendleft():
    return lst.insert(0, True)


def deq_appendleft():
    return deq.appendleft(True)


def lst_popleft():
    return lst.pop(0)


def deq_popleft():
    return deq.popleft()


def lst_extendleft():
    a = [True, 1, 'text']
    for i in range(len(a)):
        lst.insert(0, a[i])
    return lst


def deq_extendleft():
    a = [True, 1, 'text']
    return deq.extendleft(a)


# print('Сравниваем операции append, pop, extend списка и дека')
# print('Добавляем элемент в конец')
# print('lst append', timeit("lst_append()", globals=globals(), number=1000000))
# print('deq append', timeit("deq_append()", globals=globals(), number=1000000))
# print()
# print('Берем последний элемент')
# print('lst pop', timeit("lst_pop()", globals=globals(), number=1000000))
# print('deq pop', timeit("deq_pop()", globals=globals(), number=1000000))
# print()
# print('Добавляем элементы в конец')
# print('lst extend', timeit("lst_extend()", globals=globals(), number=1000000))
# print('deq extend', timeit("deq_extend()", globals=globals(), number=1000000))
'''
Сравниваем операции append, pop, extend списка и дека
Добавляем элемент в конец
lst append 0.08820679993368685
deq append 0.06889329990372062

Берем последний элемент
lst pop 0.061441400088369846
deq pop 0.0591994000133127

Добавляем элементы в конец
lst extend 0.13815119990613312
deq extend 0.12361939996480942

deque не на много, но быстрее
'''

print('Сравниваем операции appendleft, popleft, extendleft дека и соответствующих им операций списка')
print('Добавляем элемент в начало списка')
print('lst_appendleft()', timeit("lst_appendleft()", globals=globals(), number=10000))
print('deq_appendleft()', timeit("deq_appendleft()", globals=globals(), number=10000))
print()
print('Берем элемент в начале списка по индексу[0]')
print('lst_popleft()', timeit("lst_popleft()", globals=globals(), number=10000))
print('deq_popleft()', timeit("deq_popleft()", globals=globals(), number=10000))
print()
print('Добавляем элементы в начало списка')
print('lst_extendleft()', timeit("lst_extendleft()", globals=globals(), number=10000))
print('deq_extendleft()', timeit("deq_extendleft()", globals=globals(), number=10000))
'''
Сравниваем операции appendleft, popleft, extendleft дека и соответствующих им операций списка
Добавляем элемент в начало списка
lst_appendleft() 0.013630499946884811
deq_appendleft() 0.0006311000324785709

Берем элемент в начале списка по индексу[0]
lst_popleft() 0.08919980004429817
deq_popleft() 0.0005677998997271061

Добавляем элементы в начало списка
lst_extendleft() 0.11411249998491257
deq_extendleft() 0.0012362999841570854

операции appendleft, popleft, extendleft дека работают существенно быстрее соответствующих им операций списка
'''
