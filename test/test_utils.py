from src.utils import filter_operations,

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


# def sort_by_date():
#     assert
# def mask_card():
#     assert
# def mask_account():
#     assert
# def extract_value():
#     assert
# def format_date():
#     assert
#
# def show_ops():
#     assert

