"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
import collections


def main():
    hex_dict = dict16(collections.defaultdict(int))
    first = input('Введите первое число в шестнадцатиричном формате: ').upper()
    second = input('Введите второе число в шестнадцатиричном формате: ').upper()
    num_1 = func_dex(first, hex_dict)
    num_2 = func_dex(second, hex_dict)
    print(f'Сумма чисел: {first}+{second}={func_hex(num_1 + num_2, hex_dict)}')
    print(f'Произведение чисел: {first}*{second}={func_hex(num_1 * num_2, hex_dict)}')


def func_dex(s, h):
    number = 0
    num = collections.deque(s[::-1])
    for i in range(len(num)):
        number += h[num[i]] * 16 ** i
    return number


def func_hex(number, h):
    num = collections.deque()
    while number > 0:
        d = number % len(h)
        num.appendleft([i for i in h if h[i] == d][0])
        number //= len(h)
    return ''.join(num)


def dict16(d, c=0):
    a = '0123456789ABCDEF'
    if c > len(a)-1:
        return d
    d[a[c]] += c
    return dict16(d, c+1)


if __name__ == '__main__':
    main()
