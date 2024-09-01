import requests

responce = requests.get("https://playground.learnqa.ru/api/hello/2")
print(responce.text)
