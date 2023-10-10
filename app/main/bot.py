from dotenv import load_dotenv
import discord  
from discord import app_commands
from discord.ext import commands
import os 
from mcstatus import JavaServer

load_dotenv()

token = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is up, logged in as: ", bot.user)
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="ob",description="Cek Status Server OneBlock")
async def ob(interaction):
        await interaction.response.defer()
        server = JavaServer.lookup("ob.smakensa.my.id")
        try:
            status = server.status()
            await interaction.followup.send(f"Server OneBlock sedang Online 🟢 Dengan {status.players.online} pemain; {', '.join([player.name for player in status.players.sample])}")
        except Exception as e:
            await interaction.followup.send("Server OneBlock sedang Offline 🔴")

@bot.tree.command(name="sv",description="Cek Status Server Survival")
async def ob(interaction):
        await interaction.response.defer()
        server = JavaServer.lookup("survival.smakensa.my.id")
        try:
            status = server.status()
            await interaction.followup.send(f"Server Survival sedang Online 🟢 Dengan {status.players.online} pemain; {', '.join([player.name for player in status.players.sample])}")
        except TimeoutError:
            await interaction.followup.send("Server Survival sedang Offline 🔴")

@bot.tree.command(name="help",description="Bantuan Command")
async def help(interaction):
    await interaction.response.send_message("Berikut Command yang dapat digunakan:\n\n/ob - Untuk melihat status server OneBlock\n\n/sv - Untuk melihat status server Survival\n\n Made by _xylium")

bot.run(token)
