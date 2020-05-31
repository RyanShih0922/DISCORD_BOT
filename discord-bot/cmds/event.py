import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("setting.json", "r", encoding="utf8") as jfile:
  jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["Welcome_channel"]))     #channel id (not server id)
        await channel.send(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["Leave_channel"]))     #channel id (not server id)
        await channel.send(f"{member} leave!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        """
        keyword = ["陳宜鼎", "鼎鼎"]
        if msg.content in keyword:
            await msg.channel.send("小雞雞")
        """
        if msg.content == "陳宜鼎":
            await msg.channel.send("小雞雞")


def setup(bot):
    bot.add_cog(Event(bot))