
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "ππ» **Hi [{}](tg://user?id={})**,\n\nI'm ππ πΌππππ π±ππ** \n  πΈ ππ π πππππ πππ πππ π’π πππππ πππ πππππππ πππ πΈ ππ π πΏπππππ π±ππ π πππ ππ ππ π’πππ πππππ πππ ππππ ππ ππ πππππ πππππ [β€οΈ](https://telegra.ph/file/67a238112341dc2da77d9.jpg) π±π’ @Adhi0420 !"
HELP = """π·οΈ **Need Help?** π€
__(Join @cinima_lokham For Support)__

π·οΈ **Common Commands**:
\u2022 `/play` ITTS A BAD VC PLAY UPDATE LATERπ€§
\u2022 `/help` shows help for admin commands 
\u2022 `/playlist` VC SO BADπ€§
\u2022 `/song` [song name] download the song as audio @music_wrld_grp
\u2022 `/video` [yt video link] download the yt videos  @music_wrld_grp

π·οΈ **Admin Commands**:
\u2022 `/skip` [n] skip current or n where n >= 2
\u2022 `/join` join voice chat of current group
\u2022 `/leave` leave current voice chat
\u2022 `/vc` check which VC is joined
\u2022 `/stop` stop playing music
\u2022 `/radio` start radio stream
\u2022 `/stopradio` stop radio stream
\u2022 `/replay` play from the beginning
\u2022 `/clean` remove unused RAW PCM files
\u2022 `/pause` pause playing music
\u2022 `/resume` resume playing music
\u2022 `/mute` mute the VC userbot
\u2022 `/unmute` unmute the VC userbot
\u2022 `/restart` restart the bot

π·οΈ **Developer: @@Adhi0420** π
"""

@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('α΄α΄α΄ Ιͺα΄ Ι’Κα΄α΄α΄', url='https://t.me/cinima_lokham'),
        InlineKeyboardButton('Mα΄sΙͺα΄ Ι’Κα΄α΄α΄', url='https://t.me/musicfinderbotgroup'),
    ],
    [
        InlineKeyboardButton('Κα΄Κα΄α΄Κ', url='https://t.me/Unni0240'),
        InlineKeyboardButton('α΄α΄α΄ ', url='https://t.me/Adhi0420'),
    ],
    [
        InlineKeyboardButton('Κα΄Κα΄', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
