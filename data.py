from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Start Generating Session", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Back", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/itz_sandeep_shrma")],
    ]

    START = """
Hᴇʏ {}

I'ᴀᴍ {}

You Can Use Me To Generate Session String Pyrogram And Telethon. Use The Button Below To Find Out More!
Bʏ : [ꜱᴀɴᴅᴇᴇᴘ ꜱʜᴀʀᴍᴀ](https://t.me/itz_sandeep_shrma)
    """

    HELP = """
✨ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ** ✨

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ 
/help - ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ 
/start - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ 
/generate - ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ 
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ 
/restart - ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ 
"""

    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ** 

ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ʙʏ @Japanese_Userbot

ꜰʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ  : [ᴘʏᴛʜᴏɴ](https://www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ  : [ꜱᴀɴᴅᴇᴇᴘ ꜱʜᴀʀᴍᴀ](https://t.me/itz_sandeep_shrma)
    """
