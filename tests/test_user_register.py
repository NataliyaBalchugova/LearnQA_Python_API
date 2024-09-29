
import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registraion_data()

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")


    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registraion_data(email)

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email 'vinkotov@example.com' already exists", \
            f"Unexpected response content: {response.content.decode('utf-8')}"

    # def test_create_user_with_invalid_email(self):
    #     data = self.prepare_data(email='vinkotovexample.com')
    #
    #     response = requests.post(url, data=data)
    #     assert response.status_code == 400, f"Unexpected status code {response.status_code}"
    #     assert "Invalid email format" in response.content.decode("utf-8"), \
    #         f"Unexpected response content: {response.content.decode('utf-8')}"
    #
    # def test_create_user_with_short_name(self):
    #     data = self.prepare_data(first_name='a')
    #
    #     response = requests.post(url, data=data)
    #     assert response.status_code == 400, f"Unexpected status code {response.status_code}"
    #     assert "The value of 'firstName' field is too short" in response.content.decode("utf-8"), \
    #         f"Unexpected response content: {response.content.decode('utf-8')}"
    #
    # def test_create_user_with_long_name(self):
    #     data = self.prepare_data(first_name='a' * 251)
    #
    #     response = requests.post(url, data=data)
    #     assert response.status_code == 400, f"Unexpected status code {response.status_code}"
    #     assert "The value of 'firstName' field is too long" in response.content.decode("utf-8"), \
    #         f"Unexpected response content: {response.content.decode('utf-8')}"
    #
    # @pytest.mark.parametrize("missing_field", ["password", "username", "firstName", "lastName", "email"])
    # def test_create_user_without_required_field(self, missing_field):
    #     data = self.prepare_data()
    #
    #     data.pop(missing_field)
    #
    #     response = requests.post(url, data=data)
    #
    #     assert response.status_code == 400, f"Unexpected status code {response.status_code}"
    #     assert f"The following required params are missed: {missing_field}" in response.content.decode("utf-8"), \
    #         f"Unexpected response content: {response.content.decode('utf-8')}"
