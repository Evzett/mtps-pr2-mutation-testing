import pytest

from src.email_validator import is_valid_email


# --- Исходный тест (из варианта 4) -----------------------------------------

def test_valid_email():
    assert is_valid_email("user@example.com") == True


# --- Тесты, добавленные по результатам мутационного анализа ---------------

@pytest.mark.parametrize("email", [
    "user@example.com",
    "first.last@sub.domain.org",
    "a@b.c",            # минимальный корректный адрес (граница по длине)
])
def test_valid_emails_return_true(email):
    # `is True`, а не `== True`: проверяем именно тип bool
    assert is_valid_email(email) is True


@pytest.mark.parametrize("email", [
    "userexample.com",  # нет "@" -> убивает мутанты  '' in email (#4) и and->or (#7)
    "user.example.com", # нет "@", но есть несколько точек
])
def test_email_without_at_sign_is_invalid(email):
    assert is_valid_email(email) is False


@pytest.mark.parametrize("email", [
    "user@examplecom",  # нет "." -> убивает мутанты  '' in email (#6) и and->or (#7)
    "user@localhost",
])
def test_email_without_dot_is_invalid(email):
    assert is_valid_email(email) is False


@pytest.mark.parametrize("email", [
    "",                 # пустая строка
    "plainaddress",     # нет ни "@", ни "."
])
def test_email_without_at_and_dot_is_invalid(email):
    assert is_valid_email(email) is False


def test_result_is_bool_for_invalid_email():
    # Отрицательный результат должен быть именно False, а не None/0/""
    result = is_valid_email("invalid")
    assert isinstance(result, bool)
    assert result is False


def test_non_string_input_raises_type_error():
    # Функция не обрабатывает None: оператор `in` для None выбрасывает TypeError.
    # Тест фиксирует текущий контракт функции.
    with pytest.raises(TypeError):
        is_valid_email(None)
