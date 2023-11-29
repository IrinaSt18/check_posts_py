"""Написать тест с использованием pytest и requests, в котором:
Адрес сайта, имя пользователя и пароль хранятся в config.yaml
conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров
 “username" и "password" и возвращающей токен авторизации Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого пользователя, для этого выполняется get запрос по адресу
https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации в параметре "X-Auth-Token".
Для отображения постов другого пользователя передается "owner": "notMe".
http://restapi.adequateshop.com/api/authaccount/registration
http://restapi.adequateshop.com/api/authaccount/login


url = "https://test-stand.gb.ru/gateway/login"
login = "CotCat"
password = "d09da299ca"

result = requests.post(url=url,data={"username":login, "password":password})
#print(result.json()["token"])
token = result.json()["token"]

res_get = requests.get(url="https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}, params={"owner": "notMe"})
print(res_get.json())

"""

import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def create_post(token1, title1):
    with open("config.yaml", "r") as config_file:
        config_data = yaml.safe_load(config_file)

    url = config_data['url_create_post']
    headers = {"X-Auth-Token": f"{token1}"
}

    response = requests.post(url, headers=headers, params={

        "title": f"{title1}",
        "description": "Unique Description Search999",
        "content": "Some content for the new post",

    })
    return response.json()






import requests
from urllib.parse import urlencode

S = requests.Session()


def get_posts_list(auth_token2, description1):
    URL = "https://test-stand.gb.ru/api/posts"
    params = {
        "format": "json",
        "list": "posts",
        "owner": "notMe",

    }

    # Используем urlencode для корректного формирования параметров запроса
    url_with_params = f"{URL}?{urlencode(params)}"

    r = S.get(url=url_with_params, headers={"X-Auth-Token": auth_token2})

    # Проверка на успешный ответ
    r.raise_for_status()

    try:
        posts_data = r.json()["data"]
    except KeyError:
        posts_data = []

    # Добавим вывод всего ответа для отладки
    print("Full response:", r.text)

    # Формирование списка описаний постов
    descriptions = [post.get("description", "") for post in posts_data]

    return descriptions


