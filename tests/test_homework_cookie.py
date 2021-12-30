import requests
import allure


@allure.epic("Testing cookies")
class TestCookie:
    @allure.description("Testing value of cookie")
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        cookie = response.cookies
        print(f"The value for given cookie is {cookie['HomeWork']}")
        assert "HomeWork" in cookie, "Νο 'HomeWork' in cookies"
