from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAItmWD3OC0m03OLIcpSzfiJMCDxm4xJAAKFAwACH8C5V-U9VextES_XIAQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ Developed By [ᴡᴀʀʙᴏᴛᴢ](https://t.me/thewarbotZ) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☠️☠️Owner☠️☠️", url="@Umashankar31")
                  ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ👿", url="https://t.me/shayari_jok"
                    ),
                    InlineKeyboardButton(
                        "Sports Channel", url="https://t.me/Hindi_lyrics_2021"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/shayari_jok"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Umashankar(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/shayari_jok")
                ]
            ]
        )
   )
