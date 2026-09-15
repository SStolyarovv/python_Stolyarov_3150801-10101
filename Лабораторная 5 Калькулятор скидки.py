unit_price = 1500
quantity = 9

total_raw = unit_price * quantity

if total_raw < 1000:
    discount_percent = 0
elif 1000 <= total_raw <= 5000:
    discount_percent = 5
else:
    discount_percent = 10

discount_amount = (total_raw * discount_percent) / 100
final_price = total_raw - discount_amount

print("=== РАСЧЁТ СТОИМОСТИ МАТЕРИАЛОВ ===")
print(f"Цена за ед.: {unit_price} руб.")
print(f"Количество: {quantity} шт.")
print(f"Сумма без скидки: {total_raw} руб.")
print(f"Ваша скидка: {discount_percent}% (-{discount_amount} руб.)")
print(f"Итого к оплате: {final_price} руб.")
