money_total = 0
try:  # Проверка ввода, остановка в случае ошибки
    ticket_amount = int(input("Сколько билетов вы хотите купить\n"))
    if ticket_amount <= 0:
        raise ValueError

except ValueError:
    print("Введите целое число")
    exit()

for i in range(1, ticket_amount + 1):
    try:  # Проверка ввода, остановка в случае ошибки
        age = int(input(f"Укажите возрат посетителя для билета №{i}\n"))
        if age <= 0:
            raise ValueError
        elif age >= 25:
            money_total += 1390
            print("Цена билета 1390")
        elif 25 > int(age) > 18:
            money_total += 990
            print("Цена билета 990")
        else:
            print("Бесплатно")
    except ValueError:
        print("Введите целое число")
        exit()

money_total = money_total - ((money_total / 100) * 10) if ticket_amount >= 3 else money_total  # Проверка скидки
print(f"Сумма со скидкой {money_total}") if ticket_amount >= 3 else print(f"Сумма {money_total}")
