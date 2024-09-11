import requests

url = 'https://playground.learnqa.ru/api/homework_cookie'


def test_cookie():
    response = requests.get(url)
    cookie = response.cookies
    # Ввод куки
    print(cookie)
    # Проверка значения куки
    assert "HomeWork" in cookie
