temp_c = 12
#Перевод Цельсия в Фаренгейты
temp_f = temp_c * 9/5 + 32

if temp_c <= 0:
    state = "Лёд"
elif temp_c >= 100:
    state = "Пар"
else:
    state = "Жидкость"
print(f" АНАЛИЗ ТЕМПЕРАТУРЫ ")
print(f"Температура: {temp_c}°C")
print(f"В Фаренгейтах: {temp_f}°F")
print(f"Состояние воды: {state}")
