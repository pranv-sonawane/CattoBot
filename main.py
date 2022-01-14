import discord
import os
import requests
import json

client = discord.Client()
#my_secret = os.environ['pass']

# def catto_image():
  # # response = requests.get("https://api.thecatapi.com/v1/images/search")
  # json_data = json.load(response.img)
  # image = json_data[0]['i'] + " -" + json_data[0]['a']
  # return(image) 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$cat'):
        # image = catto_image()
        await message.channel.send('Hello!!!')

client.run(os.getenv('TOKEN'))