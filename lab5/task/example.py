import re
import json
with open("D:\\pp2\\lab5\\task\\raw.txt", "r", encoding='utf-8') as f:
    data = f.read()
prices = re.findall(r'(\d+) (,)(\d+)', data)
total_price = re.search(r'ИТОГО:(\d+) (,)(\d+)', data)
datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})', data)
def extract_payment_method(data):
    # Способ оплаты
    card_match = re.search(r'Банковская карта:', data)
    cash_match = re.search(r'Наличные:', data)

    if card_match:
        return "Банковская карта"
    elif cash_match:
        return "Наличные"
    return "Не указан"
print(prices)
print(total_price.group())
print(datetime_match.group())
print(extract_payment_method(data))

