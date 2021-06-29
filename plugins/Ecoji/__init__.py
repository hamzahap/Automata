import discord
import requests
import urllib
import json
from discord.ext import commands

URANDOM_ECOJI_URI = "https://jackharrhy.dev/urandom/ecoji/"

from Plugin import AutomataPlugin

class Ecoji(AutomataPlugin):
    """Sends randomly generated emojis from Jack Harrhy's Ecoji project"""
    @commands.command()
    async def ecoji(self, ctx: commands.Context, limit):
        ecojiSrc = URANDOM_ECOJI_URI + str(limit)
        ecojiTxt = urllib.request.urlopen(ecojiSrc)
        for row in ecojiTxt:
          ecojiRows = row.decode("utf-8")
          await ctx.send(ecojiRows)
