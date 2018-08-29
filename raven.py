import discord
import asyncio
import os
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix="/")

#logs on the discord bot
@client.event
async def on_ready():
	print('I am active')
	
@client.listen()
async def on_member_join(member):
	welcome_channel = discord.Object(id='484145723198406691')
	w = discord.Embed(description='**{}** has joined the Raven\'s nest!'.format(member.mention), color=discord.Colour.purple())
	w.set_author(name=member, icon_url=member.avatar_url)
	await client.send_message(welcome_channel, embed=w)

@client.listen()
async def on_message(message):
	count = 0
	channel = client.get_channel('483866400553828354')
	for members in message.author.server.members:
		count += 1
	await client.edit_channel(channel=channel, name='lobby-{}-members'.format(count))
	
@client.command(pass_context=True)
async def test(ctx, *, arg):
	await client.say(arg)

@client.listen()
async def on_message(cat):
	if cat.content == "lol":
		await client.add_reaction(cat, emoji="😂")
		
#announce command
@client.command(pass_context=True)
async def announce(ctx, channel: discord.Channel, t=None, *, d):
	coadmin = [role.name for role in ctx.message.author.roles]
	if "Co-Owner" in coadmin or "Owner" in coadmin:
		await client.delete_message(ctx.message)
		a = discord.Embed(title=t, description=d, color=discord.Colour.gold())
		a.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
		await client.send_message(channel, embed=a)
	
client.run(os.getenv('TOKEN'))
	

