from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

metrics_router = Router()


@metrics_router.message(Command("metrics"))
async def cmd_start(message: Message):
    kb = [
        [
            KeyboardButton(text="Accuracy"),
            KeyboardButton(text="Macro_f1"),
            KeyboardButton(text="All"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберете метрику"
    )
    await message.answer("Какая метрика вас интересует?", reply_markup=keyboard)


@metrics_router.message(F.text == "Accuracy")
async def with_puree(message: Message):
    await message.reply(
        "Train: 1.00\n" "Test: 1.00", reply_markup=ReplyKeyboardRemove()
    )


@metrics_router.message(F.text == "Macro_f1")
async def with_puree(message: Message):
    await message.reply(
        "Train: 1.00\n" "Test: 1.00", reply_markup=ReplyKeyboardRemove()
    )


@metrics_router.message(F.text == "All")
async def with_puree(message: Message):
    await message.reply(
        "Train Accuracy: 1.00\n"
        "Test Accuracy: 1.00\n"
        "Train Macro_f1: 1.00\n"
        "Test Macro_f1: 1.00",
        reply_markup=ReplyKeyboardRemove(),
    )
