import discord
from discord.ext import commands
import asyncio

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='r', help='Fait un rappel de 9m45s')
    @commands.has_any_role('Administrateur', 'Modérateur', 'DB player', 'SURVEILLANT SPATIAL', 'LdG', 'Admin')  # Vérifie que l'utilisateur a l'un des rôles spécifiés
    async def rappel(self, ctx):
        user = ctx.author
        
        reminder_embed = discord.Embed(
            color=0x0099ff,
            description=f"⏰ Rappel dans 9m45s <@{user.id}>\n----------------------------------\n📜 Le rappel pour ton prochain rapport est ajouté"
        )
        await ctx.send(embed=reminder_embed)

        await asyncio.sleep(9 * 60 + 45)  # 9 minutes 45 seconds

        alert_embed = discord.Embed(
            color=0x0099ff,
            description=f"👋🏻 Hey <@{user.id}> !\n---------------------------\n⏰ C'est l'heure de ton rapport !"
        )
        await ctx.send(content=f"<@{user.id}>", embed=alert_embed)

async def setup(bot):
    await bot.add_cog(Reminder(bot))
