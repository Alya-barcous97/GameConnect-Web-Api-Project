import discord
from discord.ext import commands
import random
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='send')
async def send_message(ctx):
    await ctx.send('Hello, gamers!')

@bot.command(name='joke')
async def gaming_joke(ctx):
    jokes = [
        "Why did the gamer need glasses? Because he had bad resolution.",
        "What did the gamer do when he was hungry during a long session? He went for a byte.",
        "Why was the computer cold? It left its Windows open!",
        # Add more jokes here
    ]

    random_joke = random.choice(jokes)
    await ctx.send(random_joke)

@bot.command(name='countdown')
async def countdown(ctx):
    countdown_time = 3
    for i in range(countdown_time, 0, -1):
        await ctx.send(i)
        time.sleep(1)
    
    await ctx.send('GO!')

@bot.command(name='random')
async def random_number(ctx, range_end: int):
    if range_end < 0:
        await ctx.send('Invalid range. Please provide a non-negative number.')
        return

    random_num = random.randint(0, range_end)
    await ctx.send(f'Random number: {random_num}')

@bot.command(name='motivate')
async def motivate(ctx):
    sarcastic_quotes = [
        "Don't be afraid of failure. You'll get plenty of chances.",
        "The road to success is always under construction. Enjoy the potholes.",
        "Believe in yourself, because everyone else is too busy to do it.",
        "You're not a quitter, you're just on an extended coffee break.",
        
    ]

    random_quote = random.choice(sarcastic_quotes)
    await ctx.send(random_quote)

bot.run('MTE5Nzk5NTY5MDQ0MjM2MzAyMA.Gi1CFY.RbT8vZagy0gRLD6FrOB8ED7MH0nUZGptZ634SI')
