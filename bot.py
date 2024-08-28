import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from datetime import datetime, timezone

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if not DISCORD_TOKEN:
    raise ValueError("Le token Discord n'a pas été trouvé. Assurez-vous de l'avoir défini dans un fichier .env.")

intents = discord.Intents.default()
intents.message_content = True  # Activer le contenu des messages
intents.members = True  # Activer l'intention des membres pour accéder aux rôles des utilisateurs
bot = commands.Bot(command_prefix='!', intents=intents)

# Liste des cogs à charger
COGS = [
    'cogs.reminder',
    'cogs.rappel',
    'cogs.rp',
    'cogs.issues',
    'cogs.sorciere',
    'cogs.carte',
    'cogs.rage',
    'cogs.missions',
    'cogs.regime',
    'cogs.admin'
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('Chargement des cogs...')

    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f'{cog} chargé avec succès.')
        except Exception as e:
            print(f'Erreur lors du chargement de {cog}: {e}')
    
    print('Tous les cogs ont été chargés.')

    # Synchroniser les commandes slash
    await bot.tree.sync()
    print('Commandes slash synchronisées.')

    # Changer l'état du bot
    await bot.change_presence(activity=discord.Game(name="Version 2.4"))
    print('État du bot mis à jour à "Version 2.4"')

    # ID du canal où le message doit être envoyé
    channel_id = 686257173914845205  # Remplacez par l'ID du salon cible
    channel = bot.get_channel(channel_id)
    
    if channel:
        await channel.send("Bonjour les Loups de Givre ! Je viens d'être redémarré ! Les rappels personnalisés activés avant mon redémarrage sont toujours actifs !")
        print('Message envoyé avec succès')
    else:
        print(f"Le canal avec l'ID {channel_id} n'a pas été trouvé.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Cette commande n'existe pas.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Un argument requis est manquant.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("Une erreur s'est produite lors de l'exécution de la commande.")
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send(f"{ctx.author.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.")
    else:
        await ctx.send("Une erreur inconnue s'est produite.")
    print(f'Erreur de commande: {error}')

@bot.command(name='ping', help='Répond avec Pong!')
@commands.has_any_role('Administrateur', 'Modérateur', 'DB player', 'SURVEILLANT SPATIAL', 'LdG')  # Vérifie que l'utilisateur a l'un des rôles spécifiés
async def ping(ctx):
    user = ctx.author
    bot_latency = round(bot.latency * 1000)  # Latence du bot en millisecondes

    # Envoyer un message temporaire pour mesurer la latence de l'API
    start_time = datetime.now(timezone.utc)
    api_response = await ctx.send("Mesure de la latence de l'API en cours...")
    api_latency = round((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)  # Latence de l'API en millisecondes

    # Répondre avec les détails de la latence tout en conservant le message de l'utilisateur
    embed = discord.Embed(
        title="Pong! 🏓",
        description="Détails de la latence",
        color=discord.Color.blue()
    )

    embed.add_field(name="Latence du bot", value=f"{bot_latency}ms", inline=False)
    embed.add_field(name="Latence de l'API", value=f"{api_latency}ms", inline=False)

    # Envoyer l'embed avec les détails de la latence
    await ctx.send(embed=embed)

    # Supprimer le message temporaire de mesure de latence
    await api_response.delete()

async def main():
    async with bot:
        await bot.start(DISCORD_TOKEN)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot interrompu manuellement.")
