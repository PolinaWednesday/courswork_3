from src.utils import filter_operations, sort_by_date, mask_card, mask_account, extract_value, format_date

def test_filter_operations():
    # Создаем тестовые данные
    sample_operations = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]

    # Вызываем функцию filter_operations на тестовых данных
    result = filter_operations(sample_operations)

    # Проверяем, что функция возвращает только операции со статусом "EXECUTED"
    for op in result:
        assert op["state"] == "EXECUTED"

    # Проверяем, что количество возвращенных операций совпадает с ожидаемым
    assert len(result) == 2


def test_sort_by_date():
    # Создаем тестовые данные
    sample_operations = [
        {"id": 1, "date": "2023-09-29T15:30:00.000", "description": "Operation 1"},
        {"id": 2, "date": "2023-09-28T14:30:00.000", "description": "Operation 2"},
        {"id": 3, "date": "2023-09-27T12:30:00.000", "description": "Operation 3"},
        {"id": 4, "date": "2023-09-26T11:30:00.000", "description": "Operation 4"},
     ]

    # Вызываем функцию sort_by_date на тестовых данных
    result = sort_by_date(sample_operations, num=3)

    # Проверяем, что результат отсортирован по дате в правильном порядке
    for i in range(len(result) - 1):
        assert result[i]['date'] >= result[i + 1]['date']

def test_mask_card():
    # Проверяем, что номер карты маскируется правильно
    card_number = "1234567890123456"
    masked_card = mask_card(card_number)
    assert masked_card == "1234 56** **** 3456"


def test_mask_account():
    # Проверяем, что номер счета маскируется правильно
    account_number = "1234567890"
    masked_account = mask_account(account_number)
    assert masked_account == "**7890"


def test_extract_value():
    json_list = [
        {"id": 1, "from": "MasterCard 1234567890123456"},
        {"id": 2, "to": "Счет 11112222333344445555"},
        {"id": 3}
    ]
    assert extract_value(json_list, "from") == "MasterCard 1234 56** **** 3456"
    assert extract_value(json_list, "to") == "Счет **5555"
    assert extract_value(json_list, None) == None


def test_format_date():
    assert format_date("2023-09-30T12:34:56.789") == "30.09.2023"
    assert format_date("2022-05-15T08:30:00.000") == "15.05.2022"
    assert format_date("2021-12-01T00:00:00.000") == "01.12.2021"
#
# def show_ops():
#     assert

