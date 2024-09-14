import discord
from discord import Embed
from discord.ui import Button, View
from discord.ext import commands, tasks
from itertools import cycle 
from dotenv import load_dotenv
import os

class Cleaner():
    def __init__(self):

    def ButtonListMaker(self, length:int, names:list, styles:list, emojis:list = None) -> list:
        buttonList = []

        for i in range(length):
            button = Button(label=names[i], emoji=emojis[i] if emojis else None, style=styles[i])
            buttonList.append(button)

        return buttonList

    def ButtonCallbackMatcher(self, buttonList: list, callbackList: list, View:View):
        for i in range(len(buttonList)):
            buttonList[i].callback = callbackList[i]
            View.add_item(buttonList[i])

    def GetView() -> View:
        view = View

        names = []
        emojis = []
        styles = []
        callbackNameList = []

        names.append("Shield"); emojis.append("🛡️"), styles.append(discord.ButtonStyle.blurple); callbackNameList.append("Feature")
        names.append("Break Shield"); emojis.append("🤜"), styles.append(discord.ButtonStyle.blurple); callbackNameList.append("Feature")
        names.append("Repair Shield"); emojis.append("🔨"), styles.append(discord.ButtonStyle.blurple); callbackNameList.append("Feature")
        names.append("Extra Damage"); emojis.append("🗡️"), styles.append(discord.ButtonStyle.blurple); callbackNameList.append("Feature")
        names.append("See"); emojis.append("👀"), styles.append(discord.ButtonStyle.blurple); callbackNameList.append("Feature")
        names.append("Exit"); emojis.append("👀"), styles.append(discord.ButtonStyle.red); callbackNameList.append("Exit")

        ButtonList = self.ButtonListMaker(length=12, names=names, emojis=emojis, styles=styles)      

        ButtonCallbackMatcherForGame(buttonList=ButtonList, callbackNameList=callbackNameList, View=view)