import requests

url = 'https://playground.learnqa.ru/api/homework_header'


def test_header():
    response = requests.get(url)
    header = response.headers
    print(header)
    assert "x-secret-homework-header" in header
