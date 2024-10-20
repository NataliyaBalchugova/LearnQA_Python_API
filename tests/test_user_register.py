import requests
import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase


@allure.epic("Registration cases")
class TestUserRegister(BaseCase):
    @allure.description("Test of successfully registration")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_successfully(self):
        data = self.prepare_registraion_data()

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Test of creation user with existing email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registraion_data(email)

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email 'vinkotov@example.com' already exists", \
            f"Unexpected response content: {response.content.decode('utf-8')}"
