#Comando ext!help

@client.command()
async def help(ctx):

    embed = discord.Embed(title="**Informazioni servizi**", color=0xfc0341)
    embed.add_field(name=f"Servizi 🔨", value=f"`ext!assistenza, ext!sitoweb, ext!preventivi`", inline=False)
    embed.add_field(name=f"WebSync 🌐", value=f"`ext!verifica`")
    embed.add_field(name=f"Developers 🛠️", value=f"`ext!developer`")
    embed.set_footer(text=f"Comando richiesto da: {ctx.message.author} alle: {ctime}")
    await ctx.send(embed=embed)

#Comando ext!developer

@client.command()
async def developer(ctx):
    
    embed = discord.Embed(title=f"**DEVELOPER DEL BOT**", color=0xfc0341)
    embed.add_field(name=f"DeathStrike", value=f"Mastro del web", inline=False)
    embed.add_field(name=f"Tr3cvia", value="Mastro del python", inline=False)
    await ctx.send(embed=embed)

#Comando ext!ban

@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    
    embed = discord.Embed(title=f"**BAN SYSTEM**", color=0xfc0341)
    embed.add_field(name=f"Il membro {member} è stato bannato", value=f"E' stato bannato il {ctime}", inline=False)
    await ctx.send(embed=embed)
    await member.ban(reason = reason)

    channel = client.get_channel()

#Comando ext!ban + log

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

#Log system

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

#Log system

@client.event
async def on_member_remove(member):
    channel = client.get_channel(858324584940175420)

    embed = discord.Embed(title="**LOGS SYSTEM**", color=0xfc0341)
    embed.add_field(name=f"*{member} è uscito dal server*", value="Male")
    embed.set_footer(text=f"Giorno: {ctime}")

    await channel.send(embed=embed)