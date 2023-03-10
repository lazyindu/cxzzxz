from pyrogram import Client, filters 
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Note: Lazy_Mode active β\n\n__πΆπππ ππ π πππππππ ππ πππ.__\n\nπ΄π‘πππππ:- `/set_caption {filename}\n\nπΎ Size: {filesize}\n\nβ° Duration: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__** ππΎππ π²π°πΏππΈπΎπ½ ππ°ππ΄π³ πππ²π²π΄πππ΅ππ»π»π β**__")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("Note: Lazy_Mode active β\n\nπ**Sorry sweetheart ! No Caption found...**π")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**** Your Caption deleted successfully**βοΈ")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Note: Lazy_Mode active β\n\nYour Caption:-**\n\n`{caption}`")
    else:
       await message.reply_text("π**Sorry ! No Caption found...**π")
