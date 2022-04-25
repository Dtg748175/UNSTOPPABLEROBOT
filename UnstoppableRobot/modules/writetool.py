from pyrogram import filters

from UnstoppableRobot import pbot


@pbot.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Â» É¢Éªá´ á´‡ sá´á´á´‡ á´›á´‡xá´› á´›á´ á´¡Ê€Éªá´›á´‡ Éªá´› á´É´ á´Ê á´„á´á´©Ê...")
    m = await message.reply_text("Â» á´¡á´€Éªá´› á´€ sá´‡á´„, ÊŸá´‡á´› á´á´‡ á´¡Ê€Éªá´›á´‡ á´›Êœá´€á´› á´›á´‡xá´›...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("Â» á´œá´©ÊŸá´á´€á´…ÉªÉ´É¢...")
    await pbot.send_chat_action(message.chat.id, "upload_photo")
    await message.reply_photo(hand, caption="á´¡Ê€Éªá´›á´›á´‡É´ á´¡Éªá´›Êœ ðŸ–Š Ê™Ê [Ò“á´€ÊŸÊŸá´‡É´](t.me/misslisa_robot)")


__mod_name__ = "Há´€É´á´…á´¡Ê€Éªá´›á´‡"

__help__ = """

 Writes the given text on white page with a pen ðŸ–Š

â /write <text> *:* Writes the given text.
 """
