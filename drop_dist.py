from aiogram import Router, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

image_rout = Router()


@image_rout.message(Command("photos"))
async def cmd_start(message: Message):
    kb = [
        [
            KeyboardButton(text="Возраст"),
            KeyboardButton(text="Пол"),
            KeyboardButton(text="Уровень кровяного давления"),
            KeyboardButton(text="Уровень холестерина"),
            KeyboardButton(text="Соотношения натрия к калию"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=False,
        input_field_placeholder="Выберите переменную",
    )
    await message.answer("Какая переменная вас интересует", reply_markup=keyboard)


@image_rout.message(F.text == "Возраст")
async def upload_photo(message: Message):
    image_from_pc = FSInputFile("Images/Age_dist.png")
    await message.answer_photo(image_from_pc, reply_markup=ReplyKeyboardRemove())


@image_rout.message(F.text == "Пол")
async def upload_photo(message: Message):
    image_from_pc = FSInputFile("Images/Sex_dist.png")
    await message.answer_photo(image_from_pc, reply_markup=ReplyKeyboardRemove())


@image_rout.message(F.text == "Уровень кровяного давления")
async def upload_photo(message: Message):
    image_from_pc = FSInputFile("Images/Bp_dist.png")
    await message.answer_photo(image_from_pc, reply_markup=ReplyKeyboardRemove())


@image_rout.message(F.text == "Уровень холестерина")
async def upload_photo(message: Message):
    image_from_pc = FSInputFile("Images/Ch_dist.png")
    await message.answer_photo(image_from_pc, reply_markup=ReplyKeyboardRemove())


@image_rout.message(F.text == "Соотношения натрия к калию")
async def upload_photo(message: Message):
    image_from_pc = FSInputFile("Images/Na_to_K_dist.png")
    await message.answer_photo(image_from_pc, reply_markup=ReplyKeyboardRemove())
