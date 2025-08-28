import discord
from discord.ext import commands
import asyncpg
from dotenv import load_dotenv
from os import getenv
import sys
import logging
import sqlite3

__version__ = "0.2.0"

logger = logging.getLogger(__name__)

if sys.platform != "win32":
	import uvloop
	uvloop.install()
else:
	import asyncio
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="p!", intents=discord.Intents.all(), allowed_mentions=discord.AllowedMentions.none())
bot.owner_ids = [
	513102328828788757,  # CoffeeLink
	648168353453572117,  # Pearoo
	710839743222513715,  # anchietae
	451023384151851028,  # xou
	969269703082135612,  # zypherift
	1291498084185935920, # 4831c0
]
bot.connection = sqlite3.connect("polls.db")
bot.cursor = bot.connection.cursor()
bot.cursor.execute(
	"""
	CREATE TABLE IF NOT EXISTS polls (
		poll_message_id INTEGER PRIMARY KEY,
		poll_channel_id INTEGER NOT NULL,
		log_message_id INTEGER NOT NULL
	)
	"""
)

@bot.event
async def on_ready():
	logger.info(f"Logged in as {bot.user.display_name}")

async def setup_hook():
	await bot.load_extension("log")

@bot.command()
async def reload(ctx):
	if not ctx.author.id in bot.owner_ids:
		return
	await bot.reload_extension("log")
	await ctx.send("Reloaded logging module")

bot.setup_hook = setup_hook

if __name__ == "__main__":
	bot.run(TOKEN, root_logger=True)