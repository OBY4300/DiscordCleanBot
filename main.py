import discord
from discord import Embed
from discord.ui import Button, View
from discord.ext import commands, tasks
from itertools import cycle 
from dotenv import load_dotenv
import os
import random 

#Hedef Kitle 1:
#-------------------------
#Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen gençler
#-------------------------

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

bot_status = cycle(["1", "2", "3", "4"])

load_dotenv()

SPEELS = []

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    channel = client.get_channel(1007625208443703366)
    await channel.send("Yor'ue Bluetooth Device Is Connected Successfully!")
    change_status.start()

    try:
        synced_commands = await client.tree.sync()
        print(f"Synced {len(synced_commands)} commands.")
    except Exception as e:
        print("An error with syncing application commands has occurred", e)

@client.command()
async def Atik(ctx):
    tavsiyeler = ["Aynı zamanda salğıa zararlı olan fast food tüketimini azaltabilrsin.", "Tek kullanımlık kaşık veya çatalları kullanmamayı tercih edebilirsin.", "Arta kalan yemekleri sokakta yemeği olmayanlara, hayvanlara verebilirsin veya mikro dalgada ısıtıp yiyebiliriz."]
    a = random.choice(tavsiyeler)
    await ctx.send(a)
    

    await interaction.response.send_message(f"You invited <@{player2.id}> to play.", ephemeral=True, view=))

client.run(os.getenv("TOKEN"))

