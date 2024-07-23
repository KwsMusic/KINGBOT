from pyrogram.types import InlineKeyboardButton

import config
from ANNIEMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_11"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 ʜᴇʟᴩ 🔎",
                callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(text="📨 sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="📨 ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="⛩️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⛩️",
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(text="🔥 ᴏᴡɴᴇʀ 🔥", user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(text="🇮🇳 ʟᴀɴɢᴜᴀɢᴇ 🏳️‍🌈", callback_data="bot_info_data"),
        ],
    ]
    return buttons
