from NoinoiRobot import Stark
from telethon import events, Button

PM_START_TEXT = """
**Hey i am {BOT_US}**
I am simple manager robot whos help to you for manage your group

**Click the below help button for the open help menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help & Commands", data="help")],
        [Button.url("Source Code", "GitHub.com/HYKO-XD/NOINOIROBOT")]])
       return

    if event.is_group:
       await event.reply("**I AM ALIVE ✨**")
       return
