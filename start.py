from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}")
    await message.answer(
        "Описание команд:\n"
        "/link - возвращает ссылку на датасет\n"
        "/metrics - предоставляет выбор метрики обученной модели\n"
        "/photos - позволяет получить выбор распределения данных в виде фото\n"
        "/predict - позволяет получить предсказание для одного наблюдения\n"
        "Введите данные следующим образом:\n"
        "Возраст Пол Кровяное_давление Уровень_холестерина\n"
        "Соотношение_натрия_к_калию\n"
        "Все данные пишите через пробел\n"
        "Пример ввода: "
        "/predict 31 F HIGH HIGH 25.355\n"
        "Перед вводом рекомендую ознакомиться с распределениями переменных"
    )
