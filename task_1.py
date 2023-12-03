text = input("Введите строку: ").lower()
result = {}
# Подсчитываем количество каждого символа в строке и записываем  полученные данные в словарь "result"
for symbol in text:
    result[symbol] = result.get(symbol, 0) + 1
new_text = ''
for i in text:
    if result[i] == 1:
        new_text += "("
    else:
        new_text += ")"
print(new_text)
