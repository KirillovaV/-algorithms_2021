"""
Задание 1.

Для каждой из трех задач выполнить следующее:

1) для каждой инструкции рядом в комментарии определите сложность этой инструкции
2) определите сложность алгоритма в целом

укажите сложность непосредственно в этом файле
точки, где нужно поработать вам, отмечены знаком '!!!'
Не забудтье оценить итоговую сложность каждого из трех алгоритмов.

Примечание:
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.

    Алгоритм 3:
    Создать множество из списка

    Сложность: O(n) - линейная
    """
    lst_to_set = set(lst_obj)  # O(n) - линейная, зависит от длины аргумента
    return lst_to_set  # O(1) - константная, только возвращаем значение


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: O(n^2) - квадратичная, цикл O(n) * вложение О(n)
    """
    for j in range(len(lst_obj)):          # O(n) - линейная, цикл, кол-во итераций зависит от количества элементов
        if lst_obj[j] in lst_obj[j+1:]:    # O(n) - линейная, срез О(n) + поиск O(n)
            return False                   # O(1) - константная
    return True                            # O(1) - константная


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: O(n log n) - линейно-логарифмическая, наихудшее из слогаемых
    """
    lst_copy = list(lst_obj)                 # O(n) - линейная, зависит от длины аргумента
    lst_copy.sort()                          # O(n log n) - линейно-логарифмическая, сортирова списка
    for i in range(len(lst_obj) - 1):        # O(n) - линейная
        if lst_copy[i] == lst_copy[i+1]:     # O(1) - константная, взятие эл-та по индейсу О(1) + сравнение О(1)
            return False                     # O(1) - константная
    return True                              # O(1) - константная

#############################################################################################

for j in (50, 500, 1000, 5000, 1000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
