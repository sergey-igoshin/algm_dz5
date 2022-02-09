"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

import collections


def main():
    num = int(input('Введите количество предприятий для расчета прибыли: '))
    data = companies(num)
    avg = round(sum([i.total for i in data]) / num, 2)
    companies_min_avg = ', '.join([i.name_company for i in data if i.total < avg])
    companies_max_avg = ', '.join([i.name_company for i in data if i.total > avg])
    print(f'Средняя годовая прибыль всех предприятий: {avg}')
    print(f'Предприятия, с прибылью выше среднего значения: {companies_max_avg}')
    print(f'Предприятия, с прибылью ниже среднего значения: {companies_min_avg}')


def value_quarter(c=1, profit=None):
    if profit is None:
        profit = {}
    if c > 4:
        profit['total'] = sum(profit.values())
        return profit
    profit['q' + str(c)] = int(input(f'Прибыль за {c} квартал: '))
    return value_quarter(c+1, profit)


def companies(n, count=1, company=None):
    if company is None:
        company = []
    if n < count:
        return company
    name_company = input(f'Введите название предприятия №{count}: ')
    res = value_quarter()
    COMPANY = collections.namedtuple('Company', 'name_company quarter_1 quarter_2 quarter_3 quarter_4 total')
    company.append(COMPANY(
        name_company=name_company,
        quarter_1=res.get('q1'),
        quarter_2=res.get('q2'),
        quarter_3=res.get('q3'),
        quarter_4=res.get('q4'),
        total=res.get('total')
    ))
    return companies(n, count+1, company)


if __name__ == '__main__':
    main()
