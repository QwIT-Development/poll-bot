import datetime
from typing import Union

import discord
from discord.ext import commands

class PollLog(commands.Cog):
	def __init__(self, bot: commands.Bot, logging_channel: discord.TextChannel):
		self.bot = bot
		self.logging_channel = logging_channel
		if self.logging_channel is None:
			raise Exception("Logging channel not found")
		self.polls = dict()  # will use db in the future

	@staticmethod
	def create_poll_log_message(message: discord.Message) -> str:
		poll = message.poll
		ends = poll.expires_at

		options = []
		for i, item in enumerate(poll.answers, start=1):
			emoji = str(item.emoji) if item.emoji else f"{i}\uFE0F\u20E3"
			percentage = round(item.vote_count / poll.total_votes * 100) if poll.total_votes > 0 else 0
			options.append(f"{emoji} {item.text} `{percentage}%`")

		multiple = "multiple options" if poll.multiple else "only one option"
		message = (
			f"A poll was created by **{message.author.name}** (`{message.author.id}`)."
			f"\n> **{poll.question}**"
			f"\n"
			f"\nEnds at {discord.utils.format_dt(ends, style='F')} ({discord.utils.format_dt(ends, style='R')})"
			f"\nYou can choose {multiple}."
			f"\n"
			f"\n{'\n'.join(options)}"
		)
		return message

	@commands.Cog.listener()
	async def on_message(self, message: discord.Message):
		if message.poll:
			poll_message_content = self.create_poll_log_message(message)
			poll_message = await self.logging_channel.send(poll_message_content)
			self.polls.update({message.id: poll_message})

	@commands.Cog.listener()
	async def on_poll_vote_add(self, user: Union[discord.User, discord.Member], answer: discord.PollAnswer):
		message = self.polls.get(answer.poll.message.id)
		if message is not None:
			await message.edit(content=self.create_poll_log_message(answer.poll.message) + f"\n\n{user.mention} voted for \"{answer.text}\"")

	@commands.Cog.listener()
	async def on_poll_vote_remove(self, user: Union[discord.User, discord.Member], answer: discord.PollAnswer):
		message = self.polls.get(answer.poll.message.id)
		if message is not None:
			await message.edit(content=self.create_poll_log_message(answer.poll.message) + f"\n\n{user.mention} removed their vote from \"{answer.text}\"")

	@commands.Cog.listener()
	async def on_message_edit(self, before: discord.Message, after: discord.Message):
		message = after
		if message.author.bot:
			return
		if message.poll and message.poll.is_finalised():
			poll_message = self.polls.get(message.id)
			if poll_message is not None:
				victor_answer = message.poll.victor_answer or max(message.poll.answers, key=lambda x: x.vote_count)
				poll_message_content = self.create_poll_log_message(message)
				poll_ended = (
					f"The poll has closed" + (" early" if message.poll.expires_at < datetime.datetime.now(tz=datetime.timezone.utc) else "") + "."
					f"\n## Winner"
					f"\n**{victor_answer.text}** `({round(victor_answer.vote_count / (message.poll.total_votes or 1) * 100)}%)`"
				)
				await poll_message.edit(content=poll_message_content + f"\n\n{poll_ended}")
				self.polls.pop(message.id)

async def setup(bot: commands.Bot):
	await bot.add_cog(PollLog(bot, await bot.fetch_channel(1410278509569507420)))