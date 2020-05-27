import discord


client = discord.Client()

@client.event
async def on_ready():
    print("ログイン完了")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

client.run("NzA2MDIxMzk4NzgyNTQxOTI3.XsHlMg.72m75fpqZOUvLAWBbsIZA0SEn9A")
