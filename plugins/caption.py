from pyrogram import Client, filters 
from helper.database import find, addcaption, delcaption 

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**πΆπΈππ΄ πΌπ΄ π° π²π°πΏππΈπΎπ½ ππΎ ππ΄π**\n\n**π΄ππ°πΌπΏπ»π΄ :-** **/set_caption **\n\n**π π΅πΈπ»π΄ π½π°πΌπ΄ : {filename}**\n\n**πΎ π΅πΈπ»π΄ ππΈππ΄ : {filesize}**\n\n**β° π³πππ°ππΈπΎπ½ : {duration}**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**ππΎππ π²π°πΏππΈπΎπ½ πππ²π²π΄πππ΅ππ»π»π π°π³π³π΄π³ β**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    #caption = fint(int(message.chat.id))[1]
    #if not caption:
       #return await message.reply_text("**ππΎπ π³πΎπ½'π π·π°ππ΄ π°π½π π²ππππΎπΌ π²π°πΏππΈπΎπ½...**")
    delcaption(int(message.chat.id))
    await message.reply_text("**ππΎππ π²π°πΏππΈπΎπ½ πππ²π²π΄πππ΅ππ»π»π π³π΄π»π΄ππ΄π³ **")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b>π ππΎππ π²π°πΏππΈπΎπ½ π </b>\n\n<b>`{caption}`</b>")
    else:
       await message.reply_text("**ππΎπ π³πΎπ½'π π·π°ππ΄ π°π½π π²ππππΎπΌ π²π°πΏππΈπΎπ½...**")
