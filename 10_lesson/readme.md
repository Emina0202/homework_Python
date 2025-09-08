# Проект автоматизации тестирования

Проект для автоматизации тестирования веб-приложения с использованием Selenium, Pytest и Allure.

## Установка зависимостей

```bash
#Подключите Allure
pip install allure-pytest

# запуск тестов 
pytest --alluredir allure-result

# запуск Allure
allure serve allure-result

# установка Allure Report
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

# отчет о тестах
allure serve allure-result

#выгрузка отчета
allure generate allure-result

