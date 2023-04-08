import discord, requests, os

from dotenv import load_dotenv
load_dotenv()

botToken = os.environ['DISCORD_TOKEN']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def sendToChannel(self, message, endPoint):
        res = requests.get('http://localhost:3000/' + endPoint)
        channel = message.channel
        await channel.send(res.text)


    async def on_message(self, message):

        if message.author == self.user:
            return
        
        if(message.content in ['!cat','!meow']):
            await self.sendToChannel(message, 'picture')

        elif(message.content == '!fact'):
            await self.sendToChannel(message, 'fact')

        elif(message.content == '!kittycat'):
            await message.channel.send("To get cat pictures, type: !cat or !meow\nTo get cat facts, type !fact")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(botToken)
 
