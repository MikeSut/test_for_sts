def bracket_validator(text: str):
    for i in text:
        if i not in '()[]{}':
            raise ValueError("Строка может состоять только из символов '()[]{}'")
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')

    # Возвращаем True, если строка пустая
    return not text

