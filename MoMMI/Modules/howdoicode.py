from typing import Match
from discord import Message
from MoMMI import MChannel, master, command

@command("howdoicode", "howdoicode")
async def dance(channel: MChannel, match: Match, message: Message) -> None:
    await channel.send("https://hackmd.io/@ss14/howdoicode")
