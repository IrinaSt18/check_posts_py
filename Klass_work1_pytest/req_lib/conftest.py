import pytest
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def auth_token1():
    result = requests.post(url=data["url_login"], data={"username": data["login1"], "password": data["password1"]})
    token = result.json()["token"]
    print(result.json()["token"])
    return token

@pytest.fixture()
def auth_token2():
    result = requests.post(url=data["url_login"], data={"username": data["login2"], "password": data["password2"]})
    token = result.json()["token"]
    print(result.json()["token"])
    return token


@pytest.fixture()
def title1():
    return "New Super Post777"


@pytest.fixture()
def description1():
    return "Unique Description Search999"


@pytest.fixture()
def content1():
    return "Some content for the new post"


@pytest.fixture()
def owner():
    return "notMe"








