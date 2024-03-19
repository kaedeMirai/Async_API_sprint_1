# Где найти код?
1. https://github.com/Munewxar/Async_API_sprint_1 - здесь хранится код api
2. https://github.com/Munewxar/new_admin_panel_sprint_3 - здесь хранится код etl
3. https://github.com/Munewxar/Async_API_sprint_1/tree/main/tests/functional - здесь хранится код тестов


# Примечания
1. Отсутствие ручек ".../search" - в ходе обсуждения с наставником, было решено избавиться от ручек ".../search" и добавить их функциональность в ручки ".../". Это было реализовано путем проверки параметра **query**: если он пустой, то возвращаются все фильмы, жанры или персоналии, если же параметр не пустой, то осуществляется фильтрация данных по заданной query.

# Ссылка на документацию api
1. http://0.0.0.0:8082/api/openapi#

# Инструкция по запуску проекта
1. Склонировать репозиторий

   ```
   git clone https://github.com/Munewxar/Async_API_sprint_1.git
   ```
2. Скопировать .env.example в .env (либо переименовать .env.example) и заполнить его
3. Заполнить значение **volumes** в сервисе **elastic** docker-compose.yml, указав путь к существующему volume. (Есть возможность заполнить индексы Elastic с использованием скрипта etl из https://github.com/Munewxar/new_admin_panel_sprint_3. Но для этого придется дополнительно разбираться в его запуске)
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
