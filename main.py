import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands, tasks
from discord import DMChannel
from discord import utils
from itertools import cycle
import time

intents = discord.Intents.all()
t = time.localtime()
ctime = time.strftime("%D ora: %H:%M", t)

from discord.ext.commands.errors import ChannelNotFound

client = commands.Bot(command_prefix='ext!', help_command=None, intents=intents)
status = cycle(['**BOT ESCLUSIVO CREATO DA NOI**', '**Bot Developed by DeathStrike and Tr3cvia**', '**www.externalproduction.it**', '**ext!help**', '**ext!ordine**'])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
    change_status.start()
    print(f"Loggato come: {client.user}")

@client.command()
async def help(ctx):

    embed = discord.Embed(title="**Informazioni servizi**", color=0xfc0341)
    embed.add_field(name=f"Servizi 🔨", value=f"`ext!assistenza, ext!sitoweb, ext!preventivi`", inline=False)
    embed.add_field(name=f"WebSync 🌐", value=f"`ext!verifica`")
    embed.add_field(name=f"Developers 🛠️", value=f"`ext!developer`")
    embed.set_footer(text=f"Comando richiesto da: {ctx.message.author} alle: {ctime}")
    await ctx.send(embed=embed)

@client.command()
async def developer(ctx):
    
    embed = discord.Embed(title=f"**DEVELOPER DEL BOT**", color=0xfc0341)
    embed.add_field(name=f"DeathStrike", value=f"Mastro del web", inline=False)
    embed.add_field(name=f"Tr3cvia", value="Mastro del python", inline=False)
    await ctx.send(embed=embed)

@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    
    embed = discord.Embed(title=f"**BAN SYSTEM**", color=0xfc0341)
    embed.add_field(name=f"Il membro {member} è stato bannato", value=f"E' stato bannato il {ctime}", inline=False)
    await ctx.send(embed=embed)
    await member.ban(reason = reason)
    
@client.command() 
async def assistenza(ctx):
    embed = discord.Embed(title="**ASSISTENZA**", color=0xfc0341)
    embed.add_field(name=f"Richiesta da {ctx.message.author}", value="Gli staffer sono stati appena avvisati in DM attendi qualcuno", inline=False)
    embed.set_footer(text=f"L'assistenza è stata fatta oggi il giorno: {ctime}")
    await ctx.send(embed=embed)

    channel = client.get_channel(858324584940175420)

    embed = discord.Embed(title="**LOGS SYSTEM**", color=0xfc0341)
    embed.add_field(name=f"**{ctx.message.author}** ha richiesto assistenza", value="`Lo staff è pregato di intervenire`")
    embed.set_footer(text=f"Giorno: {ctime}")

    await channel.send(embed=embed)

@client.event
async def on_member_join(member): 
    channel = client.get_channel(858324584940175420)

    embed = discord.Embed(title="**LOGS SYSTEM**", color=0xfc0341)
    embed.add_field(name=f"*{member} è entrato nel server*", value="Ottimo")
    embed.set_footer(text=f"Giorno: {ctime}")

    await channel.send(embed=embed)

    channel = client.get_channel(858411712201621544)
    embed = discord.Embed(title="**Benvenuto**")
    embed.add_field(name=f"**{member.mention}**", value="*È entrato nel server discord*")
    embed.set_footer(text=f"Giorno: {ctime}")
    await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(858324584940175420)

    embed = discord.Embed(title="**LOGS SYSTEM**", color=0xfc0341)
    embed.add_field(name=f"*{member} è uscito dal server*", value="Male")
    embed.set_footer(text=f"Giorno: {ctime}")

    await channel.send(embed=embed)

client.run('ODU4MDI3NzU1MTAyNDA0NjU4.YNYKng.N35iqss_H93RV_s-AWQCXK63WbE')