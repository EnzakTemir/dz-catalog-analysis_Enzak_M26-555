# Catalog Analysis

Анализ каталога фильмов: статистика, топы, жанры, актёры.

## Запуск

```bash
uv run catalog_analysis.py
```

## Проверка стиля

```bash
uv run ruff check .
```

## Структура

- `catalog_analysis.py` - все функции и точка входа `build_report(movies)`.
- `pyproject.toml` - зависимости и настройки ruff.
- `uv.lock` - зафиксированные версии зависимостей.

Выполнено студентом М26-555 Ензаком Темиром.
