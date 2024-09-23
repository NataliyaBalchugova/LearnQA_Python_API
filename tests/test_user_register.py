import pytest
import requests
from lib.base_case import BaseCase

url = 'https://playground.learnqa.ru/api/user/'


class TestUserRegister(BaseCase):

    def prepare_data(self, email='vinkotov@example.com', first_name='learnqa', last_name='learnqa', password='123',
                     username='learnqa'):
        data = {
            'password': password,
            'username': username,
            'firstName': first_name,
            'lastName': last_name,
            'email': email
        }
        return data

    def test_create_user_with_existing_email(self):
        data = self.prepare_data(email='vinkotov@example.com')

        response = requests.post(url, data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email 'vinkotov@example.com' already exists", \
            f"Unexpected response content: {response.content.decode('utf-8')}"

    def test_create_user_with_invalid_email(self):
        data = self.prepare_data(email='vinkotovexample.com')

        response = requests.post(url, data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert "Invalid email format" in response.content.decode("utf-8"), \
            f"Unexpected response content: {response.content.decode('utf-8')}"

    def test_create_user_with_short_name(self):
        data = self.prepare_data(first_name='a')

        response = requests.post(url, data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert "The value of 'firstName' field is too short" in response.content.decode("utf-8"), \
            f"Unexpected response content: {response.content.decode('utf-8')}"

    def test_create_user_with_long_name(self):
        data = self.prepare_data(first_name='a' * 251)

        response = requests.post(url, data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert "The value of 'firstName' field is too long" in response.content.decode("utf-8"), \
            f"Unexpected response content: {response.content.decode('utf-8')}"

    @pytest.mark.parametrize("missing_field", ["password", "username", "firstName", "lastName", "email"])
    def test_create_user_without_required_field(self, missing_field):
        data = self.prepare_data()

        data.pop(missing_field)

        response = requests.post(url, data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert f"The following required params are missed: {missing_field}" in response.content.decode("utf-8"), \
            f"Unexpected response content: {response.content.decode('utf-8')}"
