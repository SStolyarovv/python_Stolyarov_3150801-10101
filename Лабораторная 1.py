# Задача 1: Цифровой паспорт строительного объекта
# Автор: Столяров Сергей Александрович, 3150801/10101

student_name = "Столяров Сергей Александрович"
group_number = "3150801/10101"
project_name = "ЖК ЦДС Чёрная речка"
floors = 15
height = 48.0
is_residential = True
construction_year = 2025

print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {student_name}")
print(f"Группа: {group_number}")

print()

print(f"Объект: {project_name}")
print(f"Этажность: {floors} эт.")
print(f"Высота: {height} м")
print(f"Тип: {'Жилой' if is_residential else 'Нежилой'}")
print(f"Год постройки: {construction_year}")

