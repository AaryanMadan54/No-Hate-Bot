import discord
from discord.ext import commands
import random
import praw

client = commands.Bot(command_prefix='.')

hate_words = ['stupid','idiot','dumb','shutup','kys','loser']

quotes = ['Failure is a stepping stone to success','Every moment is a fresh beginning','Die with memories not dreams','Change the world by being yourself','All limitations are self imposed','One day the people that dont believe you will tell everyone how they met you','The time is always right to do what is right','The true meaning of life is to plant trees under whose shade you do not expect to sit','may your choices reflect your hopes, not your fears']

def get_quote():
  return random.choice(quotes)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')

@client.event
async def on_message(message):

  if message.author == client.user:
    return 

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  msg = message.content.lower() 

  if any(word in msg for word in hate_words):
    await message.channel.purge(limit = 1)
    await message.channel.send('Your message has been removed. Pls refrain from using such hate words')

  await client.process_commands(message)  

@client.command()
async def ping(ctx):
  await ctx.send(f'pong {round(client.latency *1000)}ms')

@client.command(aliases = ['inspire','motivate'])
async def quote(ctx):
  await ctx.send(get_quote())

@client.command(aliases = ['c'])
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit = amount)

@client.command(aliases = ['k'])
async def kick(ctx, member : discord.Member,*, reason = None):
  await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member,*, reason = None):
  await member.ban(reason = reason)

reddit = praw.Reddit(client_id = "EH0chZN1Q967QBRAIF29Bw", client_secret = "U0RMR_gMhusPm3tRM9im778k72YhiA",username = "python_praw", password = "python", user_agent = "no hate bot")

@client.command()
async def meme(ctx):
  memes = reddit.subreddit("memes").hot()
  pick_post = random.randint(1,50)
  for i in range(0,pick_post):
    submission = next(x for x in memes if not x.stickied)
  await ctx.send(submission.url)  

@client.command()
async def news(ctx):
  news = reddit.subreddit("news").hot()
  pick_post = random.randint(1,50)
  for i in range(0,pick_post):
    submission = next(x for x in news if not x.stickied)
  await ctx.send(submission.url)

@client.command()
async def music(ctx):
  music = reddit.subreddit("music").hot()
  pick_post = random.randint(1,50)
  for i in range(0,pick_post):
    submission = next(x for x in music if not x.stickied)
  await ctx.send(submission.url)

client.run('ODYxODUxODY1NjkwNjY5MTA2.YOP0GQ.ipuuQ5sWkdRXKeJNyZOh7cb_boM')