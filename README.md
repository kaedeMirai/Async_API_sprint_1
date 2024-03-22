# Проект "Онлайн Кинотеатр"

## Сервис Async API

Репозиторий для асинхронного API, предоставляющего доступ к данным, хранящимся в хранилище Elastic. Этот сервис является частью проекта "Онлайн Кинотеатр" и обеспечивает быстрый и эффективный доступ к информации о фильмах, жанрах, актёрах и других сущностях через асинхронные запросы.

## Содержание:

- [Django Admin Panel](https://github.com/kaedeMirai/new_admin_panel_sprint_1) - **Панель администратора для управления контентом**
- [ETL](https://github.com/kaedeMirai/admin_panel_sprint_3) - **Перенос данных из PostgreSQL в ElasticSearch для реализации полнотекстового поиска.**
- [Auth](https://github.com/kaedeMirai/Auth_sprint_1-2) - **Аутентификация и авторизация пользователей на сайте с системой ролей.**
- [UGC](https://github.com/kaedeMirai/ugc_sprint_1) - **Сервис для удобного хранения аналитической информации и UGC.**
- [UGC +](https://github.com/kaedeMirai/ugc_sprint_2) - **Улучшение функционала UGC внедрением CI/CD процессов и настройкой системы логирования Setnry и ELK.**
- [Notification service](https://github.com/kaedeMirai/notifications_sprint_1) - **Отправка уведомлений пользователям о важных событиях и акциях в кинотеатре.**
- [Watch Together service](https://github.com/kaedeMirai/graduate_work) - **Позволяет пользователям смотреть фильмы совместно в реальном времени, обеспечивая синхронизацию видео и чата.**

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
   git clone https://github.com/kaedeMirai/Async_API_sprint_1.git
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

