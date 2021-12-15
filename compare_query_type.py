import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Ответ на запрос без метода:{response1.status_code}")
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': 'HEAD'})
print(rf"Ответ на запрос с неверным методом:{response2.status_code}")

response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': 'GET'})
print(f"Ответ на запрос с верным методом:{response3.status_code}")

methods = [
    {"method": "GET"},
    {"method": "PUT"},
    {"method": "POST"},
    {"method": "DELETE"}
]


def request(request_type, url, method):
    if request_type == "GET":
        response4 = requests.request(request_type, url, params=method)
    else:
        response4 = requests.request(request_type, url, data=method)
    return response4


def list_of_methods(request_type, list_method):
    i = 0
    while i < len(methods):
        response = request(
            request_type,
            "https://playground.learnqa.ru/ajax/api/compare_query_type",
            list_method[i]
        )
        if request_type == list_method[i]["method"]:
            if response.status_code != 200:
                print(f"Реальный тип запроса {request_type} и метод {list_method[i]} совпадают, но сервер отвечает ошибкой")
        else:
            if response.status_code == 200:
                print(f"Тип запроса {request_type} и метод {list_method[i]} не совпадают, но сервер считает, что всё ОК")
        i += 1


m = 0
while m < len(methods):
    type_r = methods[m]["method"]
    list_of_methods(type_r, methods)
    m += 1


