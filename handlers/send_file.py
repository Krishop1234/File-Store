# (c) @AbirHasan2005 | @PredatorHackerzZ

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def reply_forward(message: Message, file_id: int):
    try:
        duck = await message.reply_text(
            f"**Files will be Deleted After 30 min ⏰**\n",
            disable_web_page_preview=True, quote=True)
        await asyncio.sleep(300)
        await duck.delete()
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await reply_forward(message, file_id)


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            duck1 = await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
            await asyncio.sleep(300)
            await duck1.delete()
            return
        elif Config.FORWARD_AS_COPY is False:
            duck2 = await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
            await asyncio.sleep(300)
            await duck2.delete()
            return
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await asyncio.sleep(2)
