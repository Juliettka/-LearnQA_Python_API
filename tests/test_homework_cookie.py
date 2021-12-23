import requests


class TestCookie:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        cookie = response.cookies
        print(f"The value for given cookie is {cookie['HomeWork']}")
        assert "HomeWork" in cookie, "Νο 'HomeWork' in cookies"

