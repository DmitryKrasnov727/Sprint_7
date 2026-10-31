import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierCreate:

    @allure.title('Создание курьера с валидными данными')
    @allure.description('Проверка кода и тела ответа.')
    def test_create_courier_account_success(self):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Если создать пользователя с логином, который уже есть, возвращается ошибка.')
    @allure.description('Проверка кода и тела ответа.')
    def test_create_courier_account_login_taken_conflict(self):
        payload = {
            'login': Data.valid_login,
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        assert response.status_code == 409 and response.json() == {'message': 'Этот логин уже используется'}

    @allure.title('Если одного из полей нет, запрос возвращает ошибку.')
    @allure.description('Проверка кода и тела ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, data=empty_credentials)
        assert response.status_code == 400 and response.json() == {'message': 'Недостаточно данных для создания учетной записи'}
