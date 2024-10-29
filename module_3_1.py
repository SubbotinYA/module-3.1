# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# создаем функцию счетчика:

calls = 0
def count_calls():
    global calls  #вызываем глобальную переменную для дальнейшей работы с ней
    calls+=1   # Вот и сам счетчик. при вызове функции переменная calls плюсуется на 1


def string_info(string):  # Создать функцию string_info с параметром string
    count_calls()  # вызываем недавно созданный счетчик
    # после активации функции string_info возвращаем значения
    return (len(string), string.upper(), string.lower())


# Создаём функцию is_contains с двумя параметрами string куда вводим слово,
# и list_to_search список из слов. т.к string ее можно использовать хоть в сотнях функциях
def is_contains(string, list_to_search):
    count_calls()  # снова вызываем счетчик
    lower_list_to_search = []  # идея создать новый список, в котором все слова из списка list_to_search
    # будут прописаны строчными буквами
    for i in list_to_search:
        lower_list_to_search.append(i.lower())
    return string.lower() in lower_list_to_search  # после поиска возвращаем логический результат


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
