money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months_without_debt = 0
current_month_capital = money_capital + salary - spend
current_month_spend = 6000

while current_month_capital >= 0:
    current_month_capital += money_capital + salary - current_month_spend
    current_month_spend += spend * (1 + increase)
    months_without_debt += 1

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt)
