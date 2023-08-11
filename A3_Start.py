import os
import discord
from datetime import datetime

# Bot's token and the target server's name
TOKEN = "MTEzOTYyNzgwNzkyNDgzMDIzMQ.Gn-Eli.tslHh55iD3DgxV0VW41YAc-KcNP3NhcCYgS0NE"
GUILD = "Bete Mauj Kardi."
fname = "memberLogon.csv"

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event 
async def on_ready():
    # Find the target guild from the bot's connected guilds
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    # If the CSV file doesn't exist, create it and log current members
    if not os.path.exists(fname):
        with open(fname, "w", encoding='utf-8') as file:
            file.write("Username,Join Date & Time\n")
            for member in guild.members:
                formatted_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                file.write(f"{member.name},{formatted_date_time}\n")

@client.event
async def on_member_join(member):
    # Log the new member's name and join time to the CSV
    with open(fname, "a", encoding='utf-8') as file:
        formatted_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        file.write(f"{member.name},{formatted_date_time}\n")

@client.event
async def on_member_remove(member):
    # Remove the member's details from the CSV when they leave the server
    with open(fname, "r") as file:
        lines = file.readlines()
    with open(fname, "w") as file:
        for line in lines:
            if line.split(",")[0] != member.name:
                file.write(line)

# Start the bot using the provided token
client.run(TOKEN)
