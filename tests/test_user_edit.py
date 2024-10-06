import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registraion_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"

        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        print(f'{user_id}')
        Assertions.assert_code_status(response3, 200)

        # GET

        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of user after edit"
        )

    def test_edit_unauthorized_user(self):
        new_name = "Unauthorized user"
        user_id = 2

        response5 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response5, 400)

    def test_edit_another_user(self):
        register_data = self.prepare_registraion_data()
        response6 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response6, 200)
        Assertions.assert_json_has_key(response6, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response6, "id")

        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response7 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response7, "auth_sid")
        token = self.get_header(response7, "x-csrf-token")

        new_name = "Another User"
        response8 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response8, 400)

    def test_edit_invalid_email(self):
        register_data = self.prepare_registraion_data()
        response9 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response9, 200)
        Assertions.assert_json_has_key(response9, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response9, "id")

        login_data = {
            'email': email,
            'password': password
        }

        response10 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response10, "auth_sid")
        token = self.get_header(response10, "x-csrf-token")

        new_email = "invalidemailexample.com"

        response11 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_code_status(response11, 400)

    def test_edit_short_first_name(self):
        register_data = self.prepare_registraion_data()
        response12 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response12, 200)
        Assertions.assert_json_has_key(response12, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response12, "id")

        login_data = {
            'email': email,
            'password': password
        }

        response13 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response13, "auth_sid")
        token = self.get_header(response13, "x-csrf-token")

        new_first_name = "A"

        response14 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_first_name}
        )

        Assertions.assert_code_status(response14, 400)
        Assertions.assert_json_value_by_name(response14,
                                             "error",
                                             "The value for field `firstName` is too short",
                                             "Wrong response message when trying to set a very short firstName"
                                             )
