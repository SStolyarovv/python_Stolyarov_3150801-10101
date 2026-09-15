contractor_1 = ["Кирпич", "Цемент", "Песок", "Арматура"]
contractor_2 = ["Цемент", "Бетон", "Доска", "Песок"]
contractor_3 = ["Песок", "Щебень", "Кирпич", "Стекло"]

set1 = set(contractor_1)
set2 = set(contractor_2)
set3 = set(contractor_3)

all_unique = set1 | set2 | set3

common_for_all = set1 & set2 & set3

only_first = set1 - (set2 | set3)

exactly_two = (set1 & set2 | set2 & set3 | set1 & set3) - common_for_all

print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Всего уникальных позиций: {all_unique}")
print(f"Общие материалы для всех: {common_for_all if common_for_all else 'Нет общих'}")
print(f"Только у первого подрядчика: {only_first}")
print(f"Материалы ровно у двух: {exactly_two}")
