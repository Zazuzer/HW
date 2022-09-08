per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_values = list(per_cent.values())

money = int(input('Введите сумму депозита \n'))

deposit = [round(i * money) for i in per_cent_values ]     #Считаем процент и округляем

print('Максимальная сумма, которую вы можете заработать — %d' % max(deposit))