import discord
import os

client = discord.Client()
from discord.ext import commands


bot = commands.Bot(command_prefix='g-')
bot.remove_command("help")
@bot.event
async def on_ready():
  print("準備完了")


bot.run(os.getenv('TOKEN'))
