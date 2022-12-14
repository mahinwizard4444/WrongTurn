from datetime import datetime 
from Script import script 
import asyncio
from info import LOG_CHANNEL
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message 

def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.command("bug"))
async def bug(bot, message):
    if message.chat.username:
        chat_username = f"@{message.chat.username}/`{message.chat.id}`"
    else:
        chat_username = f"ᴩʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴩ/`{message.chat.id}`"
    bugs = content(message)
    user_id = message.from_user.id
    if bugs:
            await message.reply_text(
                f"<b>ʙᴜɢ ʀᴇᴩᴏʀᴛ : {bugs}</b>\n\n"
                "<b>» ʙᴜɢ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴩᴏʀᴛᴇᴅ !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data=f"close_reply")]]
                ),
            )
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_B.format(bugs, message.from_user.mention, message.from_user.id))
    else: 
        ms = await message.reply_text("ɴᴏ ʙᴜɢ ᴛᴏ ʀᴇᴩᴏʀᴛ !")
        await asyncio.sleep(10)
        await message.delete()
        await ms.delete()
@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

