from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

link_router = Router()


@link_router.message(Command("link"))
async def dataset_link(message: Message):
    link = "https://www.kaggle.com/datasets/prathamtripathi/drug-classification"
    await message.answer(f"URL : {link}")
