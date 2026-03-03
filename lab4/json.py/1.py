import json

data = {
    "name": "Наташа",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "English"],
    "address": {"city": "New York", "zip": "10001"}
}

json_data = json.dumps(data, indent=4)  # Преобразуем в строку JSON с отступами
print(json_data)
import json

data = {
    "name": "Наташа",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "English"],
    "address": {"city": "New York", "zip": "10001"}
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Записываем данные в файл
