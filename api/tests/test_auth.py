import allure


@allure.title("Получение токена авторизации")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_token(auth_client):
    with allure.step("Отправляем запрос на авторизацию"):
        response = auth_client.authenticate()
        allure.attach(str(response.json()), name="Response", attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверяем, что токен получен"):
        assert "token" in response.json()


@allure.title("Неверные учетные данные")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_auth(auth_client):
    with allure.step("Авторизация с неверным логином и паролем"):
        response = auth_client.authenticate("wrong", "wrong")
        allure.attach(str(response.json()), name="Response", attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверяем сообщение об ошибке"):
        assert response.json()["reason"] == "Bad credentials"


@allure.title("Пустые учетные данные")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.MINOR)
def test_empty_auth(auth_client):
    with allure.step("Авторизация с пустыми полями"):
        response = auth_client.authenticate("", "")
        allure.attach(str(response.json()), name="Response", attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверяем статус ответа"):
        assert response.status_code == 200