# Деплой

## Схема

```text
push → CI (lint/test/build) → registry → CD → окружение
```

## Предусловия

- Настроенные секреты CI: `REGISTRY_TOKEN`, `SSH_KEY`, `DB_PASSWORD` и т.д.
- Созданная инфраструктура (`terraform apply`) — см. `infra/`

## Ручной деплой (первый раз)

```bash
# 1. Инфраструктура
cd infra/terraform/envs/dev
terraform init && terraform plan && terraform apply

# 2. Приложение
ssh <user>@<host>
cd /opt/app && docker compose pull && docker compose up -d
```

## Автоматический деплой

_Описание пайплайна: триггер (тег/merge в main), шаги, проверки._

## Проверка после деплоя

```bash
curl -fsS https://<domain>/health
```

## Откат (rollback)

```bash
# Вернуться на предыдущий образ
docker compose pull app:<previous-tag>
docker compose up -d app
```

## Runbook: что делать при инциденте

1. Проверить алерты и дашборд.
2. `docker compose logs --tail=200 app`.
3. При необходимости — откат по инструкции выше.
4. Зафиксировать инцидент в `docs/incidents.md`.
