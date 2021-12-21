import requests


class TestHeader:
    def test_homework_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"

        response = requests.get(url)
        header = response.headers
        print(f"The value for headers are {header}")
        print(header['x-secret-homework-header'])
        assert "x-secret-homework-header" in header, "Νο 'x-secret-homework-header' in headers"
        assert header['x-secret-homework-header'] == 'Some secret value', "Value is different"
