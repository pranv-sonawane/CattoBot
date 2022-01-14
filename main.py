import discord
import os
import requests
import json

client = discord.Client()
#my_secret = os.environ['pass']

# def catto_image():
#   response = requests.get("https://zenquotes.io/api/random")
#   json_data = json.load(response.text)
#   image = json_data[0]['q'] + " -" + json_data[0]['a']
#   return(image) 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$cat'):
        # image = catto_image()
        await message.channel.send('Helo!!!')

client.run(os.getenv('TOKEN'))