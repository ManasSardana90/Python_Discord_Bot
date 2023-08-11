import os
import discord
from datetime import datetime

TOKEN = "MTEzOTYyNzgwNzkyNDgzMDIzMQ.Gn-Eli.tslHh55iD3DgxV0VW41YAc-KcNP3NhcCYgS0NE"
GUILD = "Bete Mauj Kardi."
fname = "memberLogon.csv"

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event 
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    if not os.path.exists(fname):
        with open(fname, "w", encoding='utf-8') as file:
            file.write("Username,Join Date & Time\n")
            for member in guild.members:
                formatted_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                file.write(f"{member.name},{formatted_date_time}\n")

@client.event
async def on_member_join(member):
    with open(fname, "a", encoding='utf-8') as file:
        formatted_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        file.write(f"{member.name},{formatted_date_time}\n")

@client.event
async def on_member_remove(member):
    with open(fname, "r") as file:
        lines = file.readlines()
    with open(fname, "w") as file:
        for line in lines:
            if line.split(",")[0] != member.name:
                file.write(line)

client.run(TOKEN)
