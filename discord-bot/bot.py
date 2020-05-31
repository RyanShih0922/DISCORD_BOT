import discord
from discord.ext import commands
import json
import random
import os
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

with open("setting.json", "r", encoding="utf8") as jfile:
  jdata = json.load(jfile)

#bot = commands.Bot(command_prefix="!")
bot = discord.Bot(command_prefix="!")

@bot.event
async def on_ready():
  print(">> Bot is online <<")

"""
@bot.event
async def on_member_join(member):
  channel = bot.get_channel(int(jdata["Welcome_channel"]))     #channel id (not server id)
  await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(int(jdata["Leave_channel"]))     #channel id (not server id)
  await channel.send(f"{member} leave!")
"""

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f"cmds.{extension}")
  await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f"cmds.{extension}")
  await ctx.send(f"Unloaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
  bot.reload_extension(f"cmds.{extension}")
  await ctx.send(f"Reloaded {extension} done.")

"""
@bot.command()
async def ping(ctx):    #ctx = context (上下文) (included: user, id, server, channel)
  await ctx.send(f"{round(bot.latency*1000)} ms")

@bot.command()
async def clean(ctx, num: int):
  await ctx.channel.purge(limit=num+1)
"""

"""
@bot.command()
async def wiki(ctx, keyword:str):
  res = requests.get("https://zh.wikipedia.org/wiki/{}".format(keyword))
  soup = BeautifulSoup(res.text, "lxml")
  article = soup.select_one(".mw-parser-output p").text
  await ctx.send(f"{article}")

@bot.command()
async def wiki_en(ctx, keyword:str):
  res = requests.get("https://en.wikipedia.org/wiki/{}".format(keyword))
  soup = BeautifulSoup(res.text, "lxml")
  article = soup.select_one(".mw-parser-output p").text
  await ctx.send(f"{article}")

@bot.command()
async def 翻譯(ctx, keyword:str):
  translator = Translator()
  lang = "en"
  ans = translator.translate((keyword), lang).text
  await ctx.send(f"{ans}")

@bot.command()
async def trans(ctx, keyword:str):
  translator = Translator()
  lang = "zh-TW"
  ans = translator.translate((keyword), lang).text
  await ctx.send(f"{ans}")
"""


for filename in os.listdir("./cmds"):
  if filename.endswith(".py"):
    bot.load_extension(f"cmds.{filename[:-3]}")   #-3: ignore the last 3 letter (including punctuation marks)


if __name__ == "__main__":
  bot.run(os.environ["DISCORD_TOKEN"])