import discord
from discord.ext import tasks, commands
from config import settings
import json
import requests
import random

bot = commands.Bot(command_prefix=settings['prefix'], help_command=None)

@bot.command()
async def rand(ctx, *arg):
    await ctx.reply(random.randint(0, 100))

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xffffff, title = 'Random Fox')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed) 

@tasks.loop(seconds=2)
async def change_status():
    channel = bot.get_channel(992722905458814986)
    print('test')
    await channel.send('Your message')
    
@bot.command()
async def help(context):
    await context.send("```Custom help command```")
    
@bot.event
async def on_ready():
    print("Bot is Ready.")



bot.run(settings['token'])