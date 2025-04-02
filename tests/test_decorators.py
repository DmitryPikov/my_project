import pytest

from src.decorators import log


@log()
def successful_func(a: int, b: int) -> int:
    return a + b


def test_log_success() -> None:
    """Проверяет логирование успешного выполнения"""

    result = successful_func(2, 3)
    assert result == 5


@log()
def failing_func(a: int, b: int) -> float:
    return a / b


def test_log_error() -> None:
    """Проверяет логирование ошибки"""

    with pytest.raises(ZeroDivisionError):
        failing_func(1, 0)


def test_log_console_output(capsys: pytest.CaptureFixture) -> None:
    """Проверяет вывод логов в консоль"""

    @log()
    def console_log_func(x: int) -> int:
        return x * 2

    result = console_log_func(5)
    assert result == 10

    captured = capsys.readouterr()
    assert "console_log_func ok" in captured.out


def test_log_file_and_console() -> None:
    """Проверяет, что логи пишутся только в файл, если filename указан"""

    @log("log_file.txt")  # Логи только в файл
    def file_log_func(x: str) -> str:
        return f"Hello, {x}!"

    result = file_log_func("Alice")
    assert result == "Hello, Alice!"
