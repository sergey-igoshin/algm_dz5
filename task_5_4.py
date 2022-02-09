"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым из них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict


def dict_get():
    return dict_obj.get('0')


def or_dict_get():
    return or_dict_obj.get('0')


def dict_add():
    dict_obj['1'] = False
    return


def or_dict_add():
    or_dict_obj['1'] = False
    return


dict_obj = {'5': True, '20': 1, '7': 'text'}
or_dict_obj = OrderedDict({'5': True, '20': 1, '7': 'text'})

print('Операция получения значения')
print('dict_get', timeit('dict_get()', globals=globals(), number=1000000))
print('or_dict_get', timeit('or_dict_get()', globals=globals(), number=1000000))
print()
print('Операция добавления')
print('dict_add', timeit('dict_add()', globals=globals(), number=1000000))
print('or_dict_add', timeit('or_dict_add()', globals=globals(), number=1000000))
print()
dict_add()
or_dict_add()
print(dict_obj)
print(or_dict_obj)

'''
Операция получения значения
dict_get 0.06271389999892563
or_dict_get 0.06781249993946403

Операция добавления
dict_add 0.06250649993307889
or_dict_add 0.0727812999393791

{'5': True, '20': 1, '7': 'text', '1': False}
OrderedDict([('5', True), ('20', 1), ('7', 'text'), ('1', False)])

OrderedDict потерял актуальность после версии 3.6
При выводе данные упорядоченные и сюдя по замерам OrderedDict работает медленнее
'''
