import functools
from typing import Any, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор, логирующий вызовы функций"""

    def decorator(func: Any) -> Any:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                log_message = f"{func_name} ok\n"
            except Exception as e:
                inputs = f"Inputs: {args}, {kwargs}" if args or kwargs else "Inputs: ()"
                log_message = f"{func_name} error: {type(e).__name__}. {inputs}\n"
                raise
            finally:
                write_log(log_message, filename)

            return result

        return wrapper

    return decorator


def write_log(message: str, filename: Optional[str] = None) -> None:
    """Функция для вывода лога в файл или консоль"""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message, end="")
