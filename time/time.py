import discord
from discord.ext import commands
try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import aiohttp

class Timecog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self):

        #Your code will go here
        url = "http://www.worldtimeserver.com/current_time_in_UTC.aspx" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            servertime = soupObject.find(class_='fontTS').get_text()
            await self.bot.say('GMS server time is ' + servertime)
        except:
            await self.bot.say("Couldn't load server time.")

def setup(bot):
    bot.add_cog(Timecog(bot))
