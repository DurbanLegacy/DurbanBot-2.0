
https://github.com/DurbanLegacy/DurbanBot-2.0
import discord
intents = discord.Intents.all()
from discord.ext import commands
client = commands.Bot(command_prefix = "!", intents=intents, help_command = None)
import os

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='DurbanBot 2.0 is live!'))

@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))
    await ctx.send('https://gifimage.net/wp-content/uploads/2017/09/angry-anime-girl-gif.gif')

@commands.has_permissions(ban_members = True)
@client.command()
async def ban(ctx, members: commands.Greedy[discord.Member],
                   reason: str):

    for member in members:
        await member.ban(reason=reason)

@commands.has_permissions(kick_members = True)
@client.command()
async def kick(ctx, members: commands.Greedy[discord.Member],
                   reason: str):

    for member in members:
        await member.kick(reason=reason)

@client.command()
async def say(ctx, *, arg): 
    await ctx.message.delete()
    await ctx.send(arg)
    print(ctx.author.name + ' has used ' + ctx.message.content + ' In ' + ctx.channel.name)

@commands.has_permissions(manage_messages = True)
@client.command()
async def clean(ctx):
    await ctx.message.delete()
    await ctx.send('**\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****\n****')
    await ctx.send(f"Chat successfully cleared by {ctx.author.name}.")  

  

@client.listen('on_message')
async def on_message(message):
      insults = ['fuck', 'cunt', 'nigger', 'shit']

      for word in insults:
        if word in message.content.lower():
          print(message.author.name + ' said ' + message.content + ' in the channel ' + message.channel.name)
          await message.delete()
          break


        if message.content.startswith('!help'):
          embed=discord.Embed(title="Commands List", description=" ", color=0x0a0079)
          embed.set_author(name=" ")
          embed.add_field(name="!help", value="Displays a list of the available commands", inline=False)
          embed.add_field(name="!slap", value="Slap a member by mentioning someone and adding a reason at the end.", inline=False)
          embed.add_field(name="!ban", value="Ban a mentioned member with a reason at the end", inline=False)
          embed.add_field(name="!kick", value="Kick a mentioned member", inline=False)
          embed.add_field(name="Bot info", value="This bot was made by DurbanLegacy#2150 in python, with lots of help from the https://discord.gg/python/ community. This bot is also open sourced. You can find the source at https://github.com/DurbanLegacy/DurbanBot-2.0/. If using this code, please credit me.", inline=False)

          embed.set_footer(text='Requested by ' + message.author.name)
          await message.channel.send(embed=embed) 
          break
          
      



client.run(os.getenv("TOKEN"))  
