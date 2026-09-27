from ast import parse
from gc import callbacks
from pydoc import text

import aiogram
import aiosqlite
from aiogram import Router, F
from aiogram.enums import parse_mode
from  aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton, input_rich_message_media,
)

from forms import user
from forms.user import Form
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import FSInputFile
import aiohttp
import asyncio


router = Router()

subscribes = set()
async def notifaer(bot: Bot):
    while True:
        if subscribes:
            for user_id in list(subscribes):
                try:
                    await bot.send_message(user_id, "Caня хуесос")
                except Exception:
                    pass

        await asyncio.sleep(3)

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет здоровяк!\nПропишите команду: /subscribe - подписка\n/unsubscribe - отписка\n/subscribes - подписчики")

@router.message(Command("subscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    subscribes.add(user_id)

    await message.answer("Вы согласны!")


@router.message(Command("unsubscribe"))
async def unsubscribe(message: Message):
    user_id = message.from_user.id

    subscribes.discard(user_id)

    await message.answer("Вы не согласны!")


@router.message(Command("subscribes"))
async def subscribes_cmd(message: Message):
    if not subscribes:
        await message.answer("Пока никого нет!")
        return
    text = "Подписчики:\n"
    for uid in subscribes:
        text+=f"{uid}\n"
    await message.answer(text)