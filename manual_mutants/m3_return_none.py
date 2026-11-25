# Ручной мутант M3: изменение возвращаемого значения (Return Value).
# Для некорректного адреса вместо False возвращается None.
def is_valid_email(email):
    return ("@" in email and "." in email) or None
