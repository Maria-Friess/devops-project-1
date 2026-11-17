# Локальная настройка

## Требования

- Linux / macOS / WSL2
- Git
- Docker Engine + Docker Compose
- _TBD: язык/runtime приложения_

## Установка

```bash
git clone <repo-url>
cd project-root
cp .env.example .env   # заполнить значения
```

## Запуск

```bash
# Вариант 1: без контейнеров (для отладки)
# ...

# Вариант 2: Docker Compose
docker compose up -d
docker compose ps
```

## Проверка

```bash
curl -fsS http://localhost:8080/health
```

## Типовые проблемы

| Симптом | Причина | Решение |
|---------|---------|---------|
| порт занят | другой процесс | `ss -ltnp` / изменить порт в `.env` |
| БД не стартует | нет прав на volume | проверить `docker compose logs db` |

## Полезные команды

```bash
docker compose logs -f app
docker compose exec db psql -U postgres
```
