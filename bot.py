import pyromod.listen
import sys

from pyrogram import Client, enums

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    LOGGER
)


class Bot(client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"},
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()

