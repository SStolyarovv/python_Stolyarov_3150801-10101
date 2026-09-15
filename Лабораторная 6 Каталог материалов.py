materials = ["Кирпич", "Цемент", "Песок", "Щебень", "Штукатурка"]

print(f"Исходный каталог: {materials}")

print(f"Первый элемент: {materials[0]}")
print(f"Последний элемент: {materials[-1]}")
print(f"Средние элементы: {materials[1:-1]}")

materials.append("Брус")
materials.append("Клей")

removed_item = materials.pop(1)
print(f"Удален элемент: {removed_item}")

print("=== ОБНОВЛЕННЫЙ КАТАЛОГ ===")
print(f"Список: {materials}")
print(f"Количество позиций: {len(materials)}")
