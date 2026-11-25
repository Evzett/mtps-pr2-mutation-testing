# Ручной мутант M2: добавленное граничное условие (Boundary / Constant).
# Адреса длиной 5 символов и короче (например, "a@b.c") ошибочно отклоняются.
def is_valid_email(email):
    return "@" in email and "." in email and len(email) > 5
