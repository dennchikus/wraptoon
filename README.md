# 🚗 WRAP TOON — Веб-сервис студии автодетейлинга и стайлинга

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0_(Async)-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![uv](https://img.shields.io/badge/Package_Manager-uv-DE5FE9?logo=astral&logoColor=white)](https://github.com/astral-sh/uv)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Reverse_Proxy-Nginx-009639?logo=nginx&logoColor=white)](https://nginx.org/)

> **Курсовой проект / Выпускная квалификационная работа**  
> **Автор разработки:** Лебедев Кирилл Денисович  
> **Специализация:** Сервис-ориентированные системы / Программная инженерия  

---

## 📋 О проекте

**WRAP TOON** — сервис-ориентированное веб-приложение для автоматизации процессов студии стайлинга и детейлинга автомобилей (оклейка виниловой и полиуретановой плёнкой, тонирование, бронирование оптики и остекления).

Проект решает задачу автоматизации клиентского пути от расчёта предварительной сметы на интерактивном калькуляторе до фиксации заявки в базе данных и передачи её на обработку мастерам.

### Ключевой функционал:
- 🧮 **Интерактивный калькулятор сметы:** динамический расчёт стоимости работ в реальном времени на основе актуального прайс-листа из базы данных (29 базовых комбинаций услуг и деталей).
- 📱 **Многостраничный адаптивный веб-интерфейс:** стилистика неонеобрутализма с поддержкой светлой и тёмной темы (`Cyber Toon Dark`), валидацией форм и умными телефонными масками.
- 📋 **Управление заявками и консультациями:** раздельная обработка заказов с калькулятора и запросов на индивидуальную консультацию/кастомный дизайн.
- 🔐 **Безопасность и разграничение доступа:** защита служебных и административных эндпоинтов по секретному заголовку `X-Admin-Token` с защитой от атак по времени (timing attacks).
- 🛡️ **Режимы окружения (Environment Separation):** автоматическое отключение интерактивной документации Swagger UI / OpenAPI в боевом режиме (`PROD`) и доступность в режиме разработки (`DEV`).
- 🐳 **Контейнеризация и изоляция:** полная готовность к развёртыванию в Docker-контейнерах с разделением сервисов бэкенда и реляционной СУБД.

---

## 🛠 Технологический стек

### Backend & Архитектура
- **Язык программирования:** Python 3.13
- **Веб-фреймворк:** [FastAPI](https://fastapi.tiangolo.com/) (асинхронная архитектура ASGI)
- **Менеджер пакетов и окружения:** [uv](https://github.com/astral-sh/uv) — высокопроизводительный инструмент управления зависимостями нового поколения
- **ORM / База данных:** [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (AsyncIO) + драйвер [asyncpg](https://github.com/MagicStack/asyncpg)
- **Валидация и сериализация:** [Pydantic v2](https://docs.pydantic.dev/) + `pydantic-settings`
- **Миграции схемы БД:** [Alembic](https://alembic.sqlalchemy.org/)
- **Паттерны проектирования:** Repository Pattern (слой абстракции над данными), Unit of Work / DBManager (управление транзакциями сессий)

### Frontend
- **Разметка и стилизация:** Семантический HTML5, чистый CSS3 (CSS Custom Properties, Grid/Flexbox, Neobrutalism UI)
- **Логика и клиенты:** Vanilla JavaScript (ES6+), асинхронный Fetch API для взаимодействия с REST API бэкенда
- **Хранение состояния:** `localStorage` для сохранения выбранной темы оформления

### Инфраструктура и DevOps
- **СУБД:** PostgreSQL 16 (в Docker-контейнере с постоянным томом данных `postgres_data`)
- **Оркестрация:** Docker Compose
- **Reverse Proxy & Web Server:** Nginx на хосте (раздача статических файлов фронтенда, проксирование API-запросов, буферизация)
- **SSL / TLS:** Бесплатные сертификаты Let's Encrypt (Certbot)

---

## 🏛 Архитектура системы

```
                             [ Интернет / Клиенты ]
                                       │
                                       ▼ (HTTPS :443)
                    ┌─────────────────────────────────────┐
                    │      Nginx Reverse Proxy (Хост)     │
                    └───────────┬─────────────────────────┘
                                │
               ┌────────────────┴────────────────┐
               │ Статика (/frontend)             │ API Прокси (/prices, /orders...)
               ▼                                 ▼
      [ HTML / CSS / JS ]             [ 127.0.0.1:8000 ]
                                                 │
                                                 ▼
                              ┌─────────────────────────────────────┐
                              │     Docker Контейнер (FastAPI)      │
                              │             "app"                   │
                              └──────────────────┬──────────────────┘
                                                 │ Docker Network
                                                 ▼ (Порт 5432)
                              ┌─────────────────────────────────────┐
                              │    Docker Контейнер (PostgreSQL)    │
                              │             "db"                    │
                              └─────────────────────────────────────┘
```

---

## 📁 Структура проекта

```text
service-oriented-systems/
├── frontend/                     # Клиентская часть (HTML, CSS, JS)
│   ├── index.html                # Главная страница (промо, карусель работ, форма)
│   ├── calculator.html           # Калькулятор расчета услуг оклейки
│   ├── services.html             # Каталог услуг и материалов
│   ├── about.html                # О студии
│   ├── style.css                 # Стили оформления (Neobrutalism UI)
│   └── theme.js                  # Переключатель светлой/тёмной темы
├── src/                          # Исходный код бэкенда
│   ├── api/                      # Маршруты API (контроллеры)
│   │   ├── dependencies.py       # Внедрение зависимостей (DBDep, AdminDep)
│   │   ├── orders.py             # Эндпоинты заказов калькулятора
│   │   ├── consultations.py      # Эндпоинты заявок на консультацию
│   │   ├── services_details.py   # Эндпоинты прайс-листа (/prices)
│   │   ├── services.py           # Справочник услуг (Admin Only)
│   │   └── details.py            # Справочник деталей авто (Admin Only)
│   ├── models/                   # SQLAlchemy ORM-модели
│   │   ├── orders.py             # Модель заказов и консультаций
│   │   ├── services.py           # Модель услуг
│   │   ├── details.py            # Модель кузовных деталей
│   │   └── services_details.py   # Модель связок деталей, услуг и стоимости
│   ├── repositories/             # Слой репозиториев (SQLAlchemy)
│   ├── schemas/                  # Pydantic-схемы валидации запросов и ответов
│   ├── scripts/                  # Вспомогательные скрипты
│   │   └── seed.py               # Сидер первоначального наполнения базы данных
│   ├── utils/                    # Утилиты и менеджер контекста транзакций
│   │   └── db_manager.py         # DBManager (Unit of Work)
│   ├── config.py                 # Настройки приложения (Pydantic BaseSettings)
│   ├── database.py               # Инициализация движка и фабрики сессий SQLAlchemy
│   └── main.py                   # Точка входа ASGI-приложения FastAPI
├── src/migrations/               # Версионирование базы данных Alembic
├── alembic.ini                   # Конфигурация миграций Alembic
├── docker-compose.yml            # Декларативное описание сервисов Docker
├── Dockerfile                    # Сборка контейнера FastAPI на базе Python 3.13 и uv
├── .dockerignore                 # Исключения сборки Docker
├── .env.example                  # Шаблон переменных окружения
├── pyproject.toml                # Конфигурация проекта и зависимости uv
└── README.md                     # Документация проекта
```

---

## 🚀 Руководство по установке и запуску

### Вариант 1. Локальный запуск для разработки

#### 1. Клонирование репозитория
```bash
git clone https://github.com/jokesss43/service-oriented-systems.git
cd service-oriented-systems
```

#### 2. Установка зависимостей через `uv`
```bash
# Установка виртуального окружения и всех зависимостей
uv sync
```

#### 3. Настройка переменных окружения
Скопируйте файл примера `.env.example` в `.env` и настройте параметры:
```bash
cp .env.example .env
```
Пример содержимого `.env`:
```ini
MODE=DEV
SECRET_ADMIN_TOKEN=dev_secret_token

DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=krl_db

FRONTEND_PORT=5500
```

#### 4. Применение миграций и наполнение БД
```bash
# Применение миграций
uv run alembic upgrade head

# Заполнение справочников и цен (сидер)
uv run python src/scripts/seed.py
```

#### 5. Запуск сервера разработки
```bash
uv run uvicorn src.main:app --reload
```
- Документация Swagger UI будет доступна по адресу: `http://127.0.0.1:8000/docs`
- Фронтенд можно запустить через Live Server на порту `5500`.

---

### Вариант 2. Развёртывание в Docker Compose (Production)

#### 1. Запуск контейнеров базы и приложения
```bash
docker compose up -d --build
```

#### 2. Применение миграций и сидирование внутри контейнера
```bash
# Выполнение миграций схемы
docker compose exec app uv run alembic upgrade head

# Первичное наполнение базы ценами и связками
docker compose exec app uv run python src/scripts/seed.py
```

#### 3. Проверка статуса
```bash
docker compose ps
docker compose logs -f app
```
Приложение будет ожидать проксирования Nginx по локальному адресу `http://127.0.0.1:8000`.

---

## 🔒 Безопасность и REST API

Для взаимодействия фронтенда с бэкендом открыты три публичных эндпоинта:
1. `GET /prices` — получение полного актуального прайса для калькулятора.
2. `POST /orders` — отправка сформированного заказа.
3. `POST /consultations` — отправка заявки на обратный звонок и консультацию.

Все административные ручки (просмотр и удаление заказов, редактирование справочников услуг и деталей) защищены. Доступ осуществляется передачей заголовка:
```http
X-Admin-Token: <SECRET_ADMIN_TOKEN>
```
При несовпадении или отсутствии токена возвращается статус `403 Forbidden`.

---

## 📈 Перспективы развития (Roadmap)
- [ ] Интеграция с **Telegram Mini App** для оперативной приёмки и распределения заказов мастерами смены.
- [ ] Подключение Telegram-бота для мгновенных уведомлений об онлайн-заявках.
- [ ] Расширение аналитического модуля для формирования отчётности по популярным услугам.
- [ ] Интеграция платёжного шлюза для приёма предоплаты при бронировании времени бокса.
