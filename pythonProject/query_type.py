import requests

# Список HTTP-методов
methods = ['POST', 'GET', 'PUT', 'DELETE']

# 1. Запрос без параметра method
payload = {}
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
print("Response without method param:", response1.text)

# 2. Запрос с неверным HTTP-методом (например, HEAD)
payload = {"method": "method"}
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print("Response with HEAD method:", response2.text)

# 3. Запрос с правильным значением method
for method in methods:
    payload = {"method": method}
    if method == 'GET':
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    else:
        response = requests.request(method, "https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"Response with method={method} and correct method param:", response.text)

# 4. Проверка всех комбинаций методов и параметров
for actual_method in methods:
    for param_method in methods:
        payload = {"method": param_method}
        if actual_method == 'GET':
            response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
        else:
            response = requests.request(actual_method, "https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        print(f"Actual method: {actual_method}, Param method: {param_method} -> Response:", response.text)