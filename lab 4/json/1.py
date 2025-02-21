import json

# Чтение JSON-файла
with open("lab 4/json/sample-data.json", 'r') as file:

    data = json.load(file)

# Вывод заголовка таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':10} {'MTU':5}")
print("-" * 50, "-" * 20, "-" * 10, "-" * 5)

# Извлечение данных и форматированный вывод
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    # Получение значений с обработкой возможных ошибок
    dn = attributes.get("dn", "").strip()
    description = attributes.get("description", "").strip()
    speed = attributes.get("speed", "inherit").strip()
    mtu = attributes.get("mtu", "9150").strip()
    
    # Обрезка значений до нужной длины
    dn = dn[:50]
    description = description[:20]
    speed = speed[:10]
    mtu = mtu[:5]
    
    # Форматированный вывод строки данных
    print(f"{dn:50} {description:20} {speed:10} {mtu:5}")
