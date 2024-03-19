import disnake
from disnake.ext import commands

import os

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="k.", intents=disnake.Intents.all())

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        for filename in os.listdir("src/cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"src.cogs.{filename[:-3]}")
                print(filename[:-3] + " loaded")


bot = Bot()
bot.run("TOKEN")