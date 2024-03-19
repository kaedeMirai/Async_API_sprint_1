# Проект "Онлайн Кинотеатр"

Репозиторий для асинхронного API, предоставляющего доступ к данным, хранящимся в хранилище Elastic. Этот сервис является частью проекта "Онлайн Кинотеатр" и обеспечивает быстрый и эффективный доступ к информации о фильмах, жанрах, актёрах и других сущностях через асинхронные запросы.

# Где найти код?
1. https://github.com/kaedeMirai/Async_API_sprint_1 - здесь хранится код api
2. https://github.com/kaedeMirai/new_admin_panel_sprint_3 - здесь хранится код etl
3. https://github.com/kaedeMirai/Async_API_sprint_1/tree/main/tests/functional - здесь хранится код тестов

# Ссылка на документацию api
1. http://0.0.0.0:8082/api/openapi#

# Инструкция по запуску проекта
1. Склонировать репозиторий

   ```
   git clone https://github.com/kaedeMirai/Async_API_sprint_1.git
   ```
2. Скопировать .env.example в .env (либо переименовать .env.example) и заполнить его
3. Заполнить значение **volumes** в сервисе **elastic** docker-compose.yml, указав путь к существующему volume. (Есть возможность заполнить индексы Elastic с использованием скрипта etl из https://github.com/kaedeMirai/new_admin_panel_sprint_3. Но для этого придется дополнительно разбираться в его запуске)
4. В командной строке запустить проект

    ```
    docker compose up
    ```

# Инструкция по запуску тестов
1. Склонировать репозиторий

   ```
   git clone https://github.com/Munewxar/Async_API_sprint_1.git
   ```
2. Скопировать tests/functinonal/.env.example в tests/functinonal/.env (либо переименовать .env.example) и заполнить его (если это потребуется)
3. В командной строке перейти в папку tests/functional (предполагается, что вы уже находитесь в корневой папке проекта)
   ```
   cd tests/functional
   ```
4. В командной строке запустить тесты

    ```
    docker compose up --abort-on-container-exit
    ```

# Над проектом работали:

### [Стивен Альтамирано](https://github.com/Munewxar)

### [Кирилл Якименков](https://github.com/TiGrib)

### [Марат Ахметзянов](https://github.com/kaedeMirai)

