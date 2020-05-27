import discord


client = discord.Client()

@client.event
async def on_ready():
    print("ログイン完了")


client.run(.env('TOKEN'))
