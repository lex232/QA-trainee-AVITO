# Тестовое задание на позицию стажёра-QA
## qa-trainee-assignment-autmumn-2024 

Привет! Меня зовут Алексей, в этом репозитории я выолняю тестовое задание на позицию стажера QA для компании AVITO!

## Задание 1: Поиск багов по скриншоту и выставление им приоретета.

- Все баги с указанием приоритета описаны в файле TASK_1_BUGS.md
- Скришоты багов, как вложения, находятся в папке /task_1_images

## Задание 2: Составление тест-кейсов для проверки API сервиса.

## Инструкции по запуску проекта:

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:lex232/QA-trainee-AVITO.git
```
- Cоздайте виртуальное окружение:
```
python3 -m venv venv
```
- Активировать виртуальное окружение на ОС Linux:
```
source venv/bin/activate
```

- Активировать виртуальное окружение на ОС Windows:
```
venv/Scripts/activate
```    
- Ообновить пакетный менеджер
```
python3 -m pip install --upgrade pip
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```    
- Запустить тесты:
```
pytest -v
```    

## О технической реализации

Проект выполнен на фреймворке Pytest языка программирования Python. Для валидации схемы данных используется - jsonschema

### Структура проекта


### Используемые зависимости requirements.txt

- attrs==24.2.0<br>
- certifi==2024.8.30<br>
- charset-normalizer==3.3.2<br>
- colorama==0.4.6<br>
- exceptiongroup==1.2.2<br>
- idna==3.8<br>
- iniconfig==2.0.0<br>
- jsonschema==4.23.0<br>
- jsonschema-specifications==2023.12.1<br>
- packaging==24.1<br>
- pluggy==1.5.0<br>
- pytest==8.3.3<br>
- pytest-jsonschema==1.0.0a2<br>
- referencing==0.35.1<br>
- requests==2.32.3<br>
- rpds-py==0.20.0<br>
- ruamel.yaml==0.18.6<br>
- ruamel.yaml.clib==0.2.8<br>
- tomli==2.0.1<br>
- urllib3==2.2.2<br>

## Автор проекта

 Алексей Кривоносов<br>
 e-mail - alexeikrivonosov@mail.ru<br>
 Git - https://github.com/lex232