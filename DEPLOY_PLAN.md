# 🚀 План деплоя и подготовки к серверу (Production Ready)

## 📌 Текущий статус сервера (Beget VPS)
- [x] VPS поднят (Beget СПб).
- [x] Установлены Zsh + тема, Docker, Docker Compose.
- [x] Установлен **Nginx на хосте** (выбрана схема: Nginx на хосте как Reverse Proxy).
- [x] Домен добавлен на Beget и направлен на сервер.

---

## 🛠️ Задачи перед деплоем (Подготовка проекта)

### 1. Переменные окружения и конфигурация (`src/config.py`)
- [ ] Добавить в `Settings`:
  - `MODE: str = "DEV"` (`DEV` или `PROD`).
  - `SECRET_ADMIN_TOKEN: str = "..."` (секретный токен для закрытых ручек).
- [x] Создан файл шаблона `.env.example` для быстрого развёртывания на сервере (`cp .env.example .env`).

### 2. Защита ручек API (Вариант Б — Секретный заголовок)
- **Публичные ручки (доступны клиентам с сайта):**
  - `GET /prices` — прайс для калькулятора.
  - `POST /orders` — отправка заказа.
  - `POST /consultations` — отправка заявки на консультацию.
- **Закрытые ручки (только по секретному заголовку `X-Admin-Token`):**
  - Создать FastAPI зависимость (dependency) `verify_admin_token`:
    - Проверяет заголовок `X-Admin-Token` на совпадение с `settings.SECRET_ADMIN_TOKEN`.
    - При несовпадении выбрасывает `HTTPException(status_code=403, detail="Forbidden")`.
  - Защитить ручки:
    - `GET /orders`, `PATCH /orders/{id}`, `DELETE /orders/{id}`
    - `GET /consultations`, `PATCH /consultations/{id}`, `DELETE /consultations/{id}`
    - Все CRUD-ручки справочников в `/services`, `/details`, `/prices` (POST, PUT, PATCH, DELETE).

### 3. Режим работы Swagger / OpenAPI (`src/main.py`)
- [ ] Настроить инициализацию `FastAPI` с учётом `MODE`:
  - Если `settings.MODE == "PROD"`, то `docs_url=None, redoc_url=None, openapi_url=None`.
  - Если `settings.MODE == "DEV"`, то документация активна.

### 4. Dockerization
- [ ] Написать `Dockerfile` для FastAPI приложения (на базе Python 3.13-slim + установка `uv` + запуск через uvicorn).
- [ ] Написать `docker-compose.yml`:
  - Сервис `db`: PostgreSQL с сохранением данных через volume (`postgres_data`).
  - Сервис `app`: Бэкенд FastAPI (связан с `db`, порт проброшен на `127.0.0.1:8000` хоста).
- [ ] Файл `.dockerignore` (исключить `.venv`, `.git`, `.idea` и т.д.).

### 5. Конфигурация Nginx на хосте и SSL
- [ ] Настроить виртуальный хост Nginx на сервере:
  - Раздача статики фронтенда (`frontend/`).
  - Проксирование API запросов (`/prices`, `/orders`, `/consultations`, `/docs`) на `http://127.0.0.1:8000`.
- [ ] Получение бесплатного SSL сертификата через `certbot --nginx -d yourdomain.ru`.

### 6. Первоначальный запуск на сервере
- [ ] Клонирование репозитория на VPS.
- [ ] `cp .env.example .env` и заполнение боевых параметров (`MODE=PROD`, секреты, пароли).
- [ ] Запуск контейнеров: `docker compose up -d --build`.
- [ ] Выполнение миграций: `docker compose exec app uv run alembic upgrade head`.
- [ ] Первичное наполнение базы (сидер): `docker compose exec app uv run python src/scripts/seed.py`.
