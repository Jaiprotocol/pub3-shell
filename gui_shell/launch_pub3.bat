@echo off
chcp 65001 >nul

echo [RU] Запуск оболочки Pub3...
echo [EN] Launching Pub3 shell...

:: Проверка наличия Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [RU] ❌ Python не найден. Добавьте его в PATH.
    echo [EN] ❌ Python not found. Please add it to PATH.
    pause
    exit /b
)

:: Запуск GUI оболочки
python pup2shell_gui_en_SAFE_DIAG_v2.py

echo.
echo [RU] Скрипт завершён.
echo [EN] Script finished.
pause