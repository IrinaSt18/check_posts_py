"""import requests
from task2 import create_post
import yaml

def test_check_post_existence(auth_token):
    post_data = {
        "title": "New Post",
        "description": "Description of the new post",
        "content": "Content of the new post",
    }


    create_post_response = create_post(auth_token, post_data)
    created_post_id = create_post_response.get("id")


    with open("config.yaml", "r") as config_file:
        config_data = yaml.safe_load(config_file)

    params = {"owner": "notMe", "description": post_data["description"]}
    response = requests.get(config_data['url_get_posts'], headers={"X-Auth-Token": auth_token}, params=params)
    posts = response.json()

    assert post.get("description") == created_post_id for post in posts"""

# test1.py
import requests
import yaml
from task2 import get_posts_list, create_post

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)


"""def test_check_post_existence(text1, auth_token):
    #assert text1 in get_posts_list(api_url=data["url_get_posts"], auth_token="auth_token"), "Not found"
    #assert text1 in get_posts_list(auth_token)
    result = get_posts_list(auth_token)
    print(result)  # Добавьте эту строку
    assert text1 in result"""


"""def test_check_post(description1,auth_token2,owner):
    # Получение списка постов и проверка наличия поста по полю "описание"
    posts_list = get_posts_list(auth_token2)
    assert description1 in posts_list, f"Post with description '{description1}' not found
    print(f"description1: {description1}")
    print(f"auth_token2: {auth_token2}")
    posts_list = get_posts_list(auth_token2,owner)
    assert description1 in posts_list, f"Post with description '{description1}' not found"""






"""def test_check_post(description1, auth_token2, owner):
    # Получение списка постов и проверка наличия поста по полю "описание"
    print(f"description1: {description1}")
    print(f"auth_token2: {auth_token2}")
    posts_list = get_posts_list(auth_token2)
    print("Posts List:", posts_list)  # Добавляем эту строку для вывода информации о постах
    #assert description1 in posts_list, f"Post with description '{description1}' not found"
    assert any(description1 in post for post in posts_list), f"Post with description '{description1}' not found"""



def test_check_post(description1, auth_token1, auth_token2, owner, title1):
    # Получение списка постов и проверка наличия поста по полю "описание"

    create_post(auth_token1, title1)
    posts_list = get_posts_list(auth_token2, description1)

    # Посмотрим на каждый пост и его описание
    for post in posts_list:
        print(f"Checking post: {post}")
        assert description1 in posts_list, f"Post with description '{description1}' not found"

    # Если код дошел сюда, значит, все проверки прошли успешно
    assert True
