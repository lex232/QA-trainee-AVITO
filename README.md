# Тестовое задание на позицию стажёра-QA
## qa-trainee-assignment-autmumn-2024 

Привет! Меня зовут Алексей, в этом репозитории я выполняю тестовое задание на позицию стажера QA для компании AVITO!<br>

## Задание 1: Поиск багов по скриншоту и выставление им приоретета.

- Все баги с указанием приоритета описаны в файле  [BUGS_TASK_1.md](./BUGS_TASK_1.md)
- Скришоты багов, как вложения, находятся в папке /task_1_images

## Задание 2: Составление тест-кейсов для проверки API сервиса.

Тесты для проверки трех эндпоинтов
- Создание объявления
- Получение объявления по его идентификатору
- Получение всех объявлений по идентификатору продавца
<br>
Все баги с указанием приоритета описаны в файле [BUGS.md](./BUGS.md)<br>
Тест кейсы описаны в файле [TESTCASES.md](./TESTCASES.md)

## Инструкции по запуску проекта:

- Клонировать репозиторий в командной строке:
```
git clone git@github.com:lex232/QA-trainee-AVITO.git
```
- Перейдите в скачанную директорию:
```
cd QA-trainee-AVITO
```
- Cоздайте виртуальное окружение. В системе должен быть установлен интерпретатор языка Python
- Вместо команды `python` возможны также варианты: `python3` или `py`
```
python -m venv venv
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
python -m pip install --upgrade pip
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

Проект выполнен на фреймворке `Pytest` языка программирования `Python`. Для валидации схемы данных используется - `jsonschema`

### Структура проекта
<pre>
├── task_1_images - скриншоты багов
    ├── bug_1.png
    ├── ....
    └── bug_15.png
├── BUGS_TASK_1.md - баг-репорт 1 задания
├── BUGS.md - баг-репорт 2 задания
├── TESTCASES.md - тест-кейсы 2 задания
├── conftest.py - фикстуры pytest
└── tests - файлы тестов
    ├── test_get_all_announcements_for_seller.py
    └── test_get_single_announcement.py
└── schemes - модуль схем валидации
    ├── __init__.py
    └── schemes.py
└── api - модуль запроса requests
    ├── __init__.py
    └── api.py
├── requirements.txt - зависимости Python
└── README.md - описание проекта
</pre>
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