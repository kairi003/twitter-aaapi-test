client = discord.Client()

@client.event
async def on_ready():
    print("ログイン完了")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("こんにちは！"):
        await message.channel.send("こんにちは！")
    if message.content.startswith("よし"):
        await message.channel.send("どうでしたか？")
    if message.content.startswith("ふぅ"):
        await message.channel.send("おつかれさん")
    if message.content.startswith("ああ"):
        await message.channel.send("どうした？")
    if message.content.startswith("こんばんは！"):
        await message.channel.send("こんばんは！")

client.run("NzA2MDIxMzk4NzgyNTQxOTI3.Xq0LwA.cEDHfQG3gpI9uA4aHWhiCTeSLyM")