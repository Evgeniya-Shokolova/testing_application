import os
import subprocess

import pytest

import constants


def test_install_application():
    """
    Проверяет, успешно ли устанавливается приложение.
    """
    print("Начало установки...")
    try:
        result = subprocess.run(
            [constants.app_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        assert result.returncode == 0, "Приложение не установлено успешно."
        print("Установка прошла успешно:", result.stdout.decode())
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Ошибка установки приложения: {e.stderr.decode()}")
    except OSError as e:
        pytest.fail(f"Ошибка OS (возможно файл повреждён или недоступен): {e}")


def test_is_app_running():
    """
    Проверяет, запускается ли приложение и корректно ли оно работает.
    """
    print(f"Пытаемся запустить: {constants.app_path}")
    assert os.path.exists(constants.app_path), "Приложение не найдено."

    try:
        result = subprocess.run([constants.app_path], check=True)
        print("Приложение успешно запущено.")
        assert result.returncode == 0, "Приложение завершилось с ошибкой."
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Ошибка запуска приложения: {e}")
    except OSError as e:
        pytest.fail(f"Ошибка OS (возможно файл повреждён или недоступен): {e}")
