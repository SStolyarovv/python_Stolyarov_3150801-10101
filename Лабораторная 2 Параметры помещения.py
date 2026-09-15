#Параметры стен
length = 10.0
width = 15.0
height = 3.5
#Стоимость квадратного метра
price_per_sq_m = 125
#Расчеты
floor_area = length * width

walls_area = 2 * height * (length + width)

volume = length * width * height

total_cost = walls_area * price_per_sq_m

print(" ПАРАМЕТРЫ ПОМЕЩЕНИЯ ")
print(f"Площадь пола: {round(floor_area, 2)} м2")
print(f"Площадь стен: {round(walls_area, 2)} м2")
print(f"Объём: {round(volume, 2)} м3")
print(f"Стоимость покраски стен: {round(total_cost, 2)} руб.")