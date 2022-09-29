import random

try:  # Проверка ввода
    nums_input = input('Введите последовательность целых чисел через пробел\n')
    control_number = input('Введите контрольное целое число\n')


    def number_check(str):
        str = str.replace(' ', '')
        try:
            int(str)
            return True
        except ValueError:
            return False


    if " " not in nums_input:
        print('Отсутствуют пробелы')
    if not number_check(nums_input):
        print('Данные не соответствуют условиям\n')
    elif not number_check(control_number):
        print('Данные не соответствуют условиям\n')
    else:
        nums_input = nums_input.split()
        control_number = int(control_number)

except ValueError:
    print("Данные не соответствуют условиям, перезапустите ПО")
    exit()

int_nums_input = [int(x) for x in nums_input]  # Строковые значения в числа


def quicksort(nums):  # Функция сортировки
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


int_nums_lst = quicksort(int_nums_input)

print(f'Упорядоченный по возрастанию список: {int_nums_lst}')


def nearest_value(int_nums_lst, control_number):  # Поиск ближайшего числа
    found = int_nums_lst[0]
    for item in int_nums_lst:
        if abs(item - control_number) < abs(found - control_number):
            found = item
    return found

min_in_list = nearest_value(int_nums_lst, control_number)

print(f'''Ближайшее число к {control_number} в списке {int_nums_lst} является {min_in_list} ''')
