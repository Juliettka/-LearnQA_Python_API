import allure
import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("Testing registration")
@allure.feature("Registration")
class TestUserRegister(BaseCase):
    @allure.description("Test is trying to create user")
    @allure.severity(severity_level="CRITICAL")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Test is trying to create user with existing email")
    @allure.severity(severity_level="NORMAL")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@xample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.description("Test is trying to create user with not valid email")
    @allure.severity(severity_level="NORMAL")
    def test_create_user_with_not_valid_email(self):
        email = 'juliatestxample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    data = [
            {
                "username": "",
                "firstName": "FirstName",
                "lastName": "LastName",
                "email": "test@example.com",
                "password": "1234"
            },
            {
                "username": "UserName",
                "firstName": "",
                "lastName": "LastName",
                "email": "test@example.com",
                "password": "1234"
            },
            {
                "username": "UserName",
                "firstName": "FirstName",
                "lastName": "",
                "email": "test@example.com",
                "password": "1234"
            },
            {
                "username": "UserName",
                "firstName": "FirstName",
                "lastName": "LastName",
                "email": "",
                "password": "1234"
            },
            {
                "username": "UserName",
                "firstName": "FirstName",
                "lastName": "LastName",
                "email": "test@test.com",
                "password": ""
            }
        ]

    @pytest.mark.parametrize('data', data)
    @allure.description("Test is trying to create user without some fields")
    @allure.severity(severity_level="LOW")
    def test_create_user_without_some_fields(self, data):
        response2 = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response2, 400)

    @allure.description("Test is trying to create user with short name")
    @allure.severity(severity_level="LOW")
    def test_create_user_with_short_name(self):
        data = self.prepare_registration_data()
        data['firstName'] = "j"

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'firstName' field is too short", f"Unexpected response content {response.content}"

    @allure.description("Test is trying to create user with long name")
    @allure.severity(severity_level="LOW")
    def test_create_user_with_long_name(self):
        data = self.prepare_registration_data()
        data['firstName'] = "j"*251

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'firstName' field is too long", f"Unexpected response content {response.content}"
