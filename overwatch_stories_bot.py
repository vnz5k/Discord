import os
import random
from discord import Intents
from discord.ext import commands, tasks
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = 'MTA5MDg3OTAwMDA4NTI4Njk1Mg.GSC9cT.YSmV605983dF9Xldb_d0xYjIGAay6JjjMDG3xk'  # Reemplaza esto con el token de tu bot
CHANNEL_ID = 1034972065918365738   # Reemplaza esto con el ID del canal donde quieres que el bot publique las historias

intents = Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

overwatch_characters = ['D.Va', 'Reaper', 'Tracer', 'Mercy', 'Winston', 'Symmetra', 'Genji', 'Hanzo', 'Lucio', 'Bastion', 'Zarya', 'McCree']

def generate_story():
    protagonist = random.choice(overwatch_characters)
    setting = random.choice(['King\'s Row', 'Hanamura', 'Temple of Anubis', 'Volskaya Industries'])
    event = random.choice(['un ataque sorpresa', 'un torneo de habilidades', 'un enfrentamiento épico', 'una misión de rescate'])

    story = f'En {setting}, {protagonist} estaba involucrado en {event}. A medida que la batalla se intensificaba...'
    return story

@tasks.loop(hours=24)
async def post_story():
    channel = bot.get_channel(CHANNEL_ID)
    story = generate_story()
    await channel.send(story)

@post_story.before_loop
async def before_post_story():
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    print(f'{bot.user} se ha conectado a Discord.')
    post_story.start()

bot.run(TOKEN)
 
