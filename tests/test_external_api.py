from unittest.mock import MagicMock, patch

from src.external_api import get_exchange_amount


def test_get_exchange_amount():
    with patch("os.getenv") as mock_getenv, patch("requests.request") as mock_request:
        # Мокируем os.getenv для возврата API ключа
        mock_getenv.return_value = "test_api_key"

        # Мокируем ответ от requests.request
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 7500.0}
        mock_request.return_value = mock_response

        # Вызываем функцию
        result = get_exchange_amount("USD", "100")

        # Проверяем, что функция вернула ожидаемый результат
        assert result == 7500.0

        # Проверяем, что requests.request был вызван с правильными параметрами
        mock_request.assert_called_once_with(
            "GET",
            "https://api.apilayer.com/exchangerates_data/convert",
            headers={"apikey": "test_api_key"},
            params={"amount": "100", "from": "USD", "to": "RUB"},
        )


if __name__ == "__main__":
    test_get_exchange_amount()
    print("Тест пройден успешно!")
