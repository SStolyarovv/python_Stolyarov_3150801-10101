addresses = [
    "  г. Москва, ул. Ленина, д. 10 ",
    "г.Казань,ул.Баумана,д.15",
    " г.Санкт-Петербург, ул. Невский, д. 100 "
]

print("=== СРАВНЕНИЕ АДРЕСОВ ===")

for i, addr in enumerate(addresses, 1):
    cleaned = addr.strip()

    cleaned = cleaned.replace("г.", "г. ").replace("ул.", "ул. ").replace("д.", "д. ")
    cleaned = cleaned.replace("  ", " ")  # Убираем двойные пробелы, если они появились

    print(f"#{i}")
    print(f"ДО: '{addr}'")
    print(f"ПОСЛЕ: '{cleaned}'")
    print("-" * 20)
