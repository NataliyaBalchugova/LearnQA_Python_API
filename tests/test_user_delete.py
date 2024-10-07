import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestUserDelete(BaseCase):
    def test_delete_user(self):
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")

        response2 = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}",
                                    headers={"x-csrf-token": token},
                                    cookies={"auth_sid": auth_sid}
                                    )

        Assertions.assert_code_status(response2, 400)

    def test_delete_created_user(self):
        register_data = self.prepare_registraion_data()
        response3 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response3, "id")

        login_data = {
            'email': email,
            'password': password
        }
        response4 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response4, "auth_sid")
        token = self.get_header(response4, "x-csrf-token")

        response4 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 200)

        response5 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response5, 404)

    def test_delete_user_as_another_user(self):
        register_data_1 = self.prepare_registraion_data()
        response6 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data_1)

        Assertions.assert_code_status(response6, 200)
        Assertions.assert_json_has_key(response6, "id")

        user_id_1 = self.get_json_value(response6, "id")
        email_1 = register_data_1['email']
        password_1 = register_data_1['password']

        register_data_2 = self.prepare_registraion_data()
        response7 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data_2)

        Assertions.assert_code_status(response7, 200)
        Assertions.assert_json_has_key(response7, "id")

        email_2 = register_data_2['email']
        password_2 = register_data_2['password']

        login_data_2 = {
            'email': email_2,
            'password': password_2
        }
        response8 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data_2)

        auth_sid_2 = self.get_cookie(response8, "auth_sid")
        token_2 = self.get_header(response8, "x-csrf-token")

        response9 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id_1}",
            headers={"x-csrf-token": token_2},
            cookies={"auth_sid": auth_sid_2}
        )

        Assertions.assert_code_status(response9, 400)
