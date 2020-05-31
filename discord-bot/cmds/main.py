import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
import os
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} ms")

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def wiki(self, ctx, keyword:str):
        res = requests.get("https://zh.wikipedia.org/wiki/{}".format(keyword))
        soup = BeautifulSoup(res.text, "lxml")
        article = soup.select_one(".mw-parser-output p").text
        await ctx.send(f"{article}")

    @commands.command()
    async def wiki_en(self, ctx, keyword:str):
        res = requests.get("https://en.wikipedia.org/wiki/{}".format(keyword))
        soup = BeautifulSoup(res.text, "lxml")
        article = soup.select_one(".mw-parser-output p").text
        await ctx.send(f"{article}")

    @commands.command()
    async def 翻譯(self, ctx, keyword:str):
        translator = Translator()
        lang = "en"
        ans = translator.translate((keyword), lang).text
        await ctx.send(f"{ans}")

    @commands.command()
    async def trans(self, ctx, keyword:str):
        translator = Translator()
        lang = "zh-TW"
        ans = translator.translate((keyword), lang).text
        await ctx.send(f"{ans}")


def setup(bot):
    bot.add_cog(Main(bot))