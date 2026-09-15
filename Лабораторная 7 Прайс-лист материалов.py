prices = {
    "Кирпич": 100,
    "Цемент": 15,
    "Песок": 7,
    "Арматура": 111,
    "Бетон": 555
}


prices["Доска"] = 650
prices["Гвозди"] = 152

prices["Цемент"] = prices["Цемент"] * 1.1

prices.pop("Песок")

all_prices = prices.values()
average_price = sum(all_prices) / len(all_prices)


print(f"{prices}")
print(f"Средняя цена материалов: {round(average_price, 2)} руб.")
