import json
import random
from random import randint
import discord
import requests
from bs4 import BeautifulSoup
import bs4
from webserver import keep_alive
import os

from webserver import *

list_cards = []

r = requests.get("https://royaleapi.github.io/cr-api-data/json/cards.json")
data = r.json()

for cards in data:
    
    list_cards.append(cards["id"])

l = randint(1, 102)

y = data[l]

print(y["id"])
print(y["elixir"])

class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(name='Type rr.deck'))
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        
        if message.content.startswith('rr.deck'):
            link = 'https://link.clashroyale.com/deck/en?deck='
            repeat = True
            while repeat == True:
                used = []
                elixir = []
                names = []
                for i in range(8):
                    y = randint(1, 102)
                    z = data[y]
                    elixir.append(z["elixir"])
                    names.append(z["name"])
                    
                    
                    used.append(i)
                    link += str(z["id"])
                    link += ';'


                if len(names) == len(set(names)):
                    repeat = False
                    average = sum(elixir) /len(elixir)
                else:
                    print(link)
                    link = 'https://link.clashroyale.com/deck/en?deck='
                    print("DUPLICATE")
                    print(names)


            link2 = link[0: -1]

            embedVar = discord.Embed(title="Random Deck", description='[Click here to copy deck!]({})'.format(link2), color=0x00ff00)
            embedVar.add_field(name="Elixir Average", value=average, inline=False)
            await message.channel.send(embed=embedVar)









keep_alive()
TOKEN = os.environ['secret_token']

client = MyClient()
client.run(TOKEN)


