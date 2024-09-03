import requests
import time

# Создание задачи
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
data_from_json = response.json()
# Запрос с token ДО того, как задача готова
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=dict(
    token=data_from_json["token"]))
status = response.json()
assert status["status"] == "Job is NOT ready"
# Ожидание
time.sleep(data_from_json['seconds'])
# Запрос c token ПОСЛЕ того, как задача готова
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=dict(
    token=data_from_json["token"]))
latest_status = response.json()
assert latest_status['status'] == 'Job is ready'
assert 'result' in latest_status
print("После ожидания:", latest_status['status'])
print("Результат:", latest_status['result'])
