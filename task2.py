salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
needed_money_capital = 0
current_month = 0
while current_month < months:
    needed_money_capital += salary
    needed_money_capital -= spend
    spend += spend * increase
    current_month += 1

rounded_money_capital = round(needed_money_capital) * -1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", rounded_money_capital)
