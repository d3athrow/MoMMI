from typing import Match
from discord import Message
from MoMMI import MChannel, master, command

@command("gettingstarted", "gettingstarted")
async def dance(channel: MChannel, match: Match, message: Message) -> None:
    await channel.send("https://hackmd.io/@ss14/getting-set-up")
