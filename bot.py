import discord
import responses
from dotenv import load_dotenv
import os

load_dotenv()

async def send_message(message):
    try:
        response = responses.handle_response()
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_bot():
    TOKEN = os.getenv('BOT_TOKEN')

    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print("Ready to HATE shayan! :)")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)

        if(username == "vizardxx"):
            await send_message(message)


    client.run(TOKEN)