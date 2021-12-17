import requests
import time

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'
response = requests.get(url)


token = response.json()["token"]
seconds = response.json()["seconds"]


response_get_task = requests.get(url, params={"token": token})

if response_get_task.json()["status"] == 'Job is NOT ready':
    print('Задача еще не готова')
    time.sleep(100)
    response_get_task_again = requests.get(url, params={"token": token})
    if response_get_task_again.json()["status"] == 'Job is ready':
        print(f"Поле result = {response_get_task_again.json()['result']}")
    else:
        print('Задача еще не готова или поле result отсутствует')


