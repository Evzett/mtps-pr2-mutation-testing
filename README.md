# Практическая работа №2. Мутационное тестирование (вариант 4: Email Validator)

Учебный проект: функция `is_valid_email()` — простая проверка email (наличие `@` и `.`).
Инструменты (по заданию): Python, pytest, MutPy (`mut.py`).

## Структура

```
src/email_validator.py            тестируемый код (не изменялся)
tests/test_email_validator.py     набор тестов (улучшенный)
manual_mutants/                   3 ручных мутанта и скрипт их прогона
results/                          сохранённые логи всех запусков
```

## Запуск

MutPy 0.6.1 поддерживает Python ≤ 3.7, поэтому используется Python 3.7.

```bash
python3.7 -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt     # Linux/macOS: .venv/bin/python

# unit-тесты + покрытие
.venv/Scripts/python -m pytest -v --cov=src --cov-report=term-missing tests

# мутационное тестирование
.venv/Scripts/python .venv/Scripts/mut.py --target src.email_validator \
    --unit-test tests.test_email_validator --runner pytest -m --show-mutants

# ручные мутанты
.venv/Scripts/python manual_mutants/run_manual_mutants.py
```

## Результаты

| Набор тестов | Тестов | Покрытие строк | Мутантов | Убито | Выжило | Mutation score |
|---|---|---|---|---|---|---|
| Исходный   | 1  | 100 % | 7 | 4 | 3 | **57,1 %** |
| Улучшенный | 12 | 100 % | 7 | 7 | 0 | **100 %** |

Ручные мутанты (M1 — удаление условия, M2 — граничное условие по длине,
M3 — возврат `None` вместо `False`): исходный набор убивает 0 из 3, улучшенный — 3 из 3.
