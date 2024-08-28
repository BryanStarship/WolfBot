import discord
from discord.ext import commands
from discord import app_commands
import asyncio

class Rappel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='z', description='Fait un rappel de 9m45s')
    async def rappel(self, interaction: discord.Interaction):
        user = interaction.user
            # Vérification des rôles
        if not any(role.name in ['role1', 'role2'] for role in user.roles): #Vérifie que l'utilisateur a l'un des rôles spécifiés (Les rôles doivent être écrit comme ceci : 'Role1', 'Role2' ect)
            await interaction.response.send_message(
                f"{user.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.", ephemeral=True)
            return
        reminder_embed = discord.Embed(
            color=0x0099ff,
            description=f"⏰ Rappel dans 9m45s <@{user.id}>\n----------------------------------\n📜 Le rappel pour ton prochain rapport est ajouté"
        )
        await interaction.response.send_message(embed=reminder_embed)

        await asyncio.sleep(9 * 60 + 45)  # 9 minutes 45 seconds

        alert_embed = discord.Embed(
            color=0x0099ff,
            description=f"👋🏻 Hey <@{user.id}> !\n---------------------------\n⏰ C'est l'heure de ton rapport !"
        )
        await interaction.followup.send(content=f"<@{user.id}>", embed=alert_embed)

async def setup(bot):
    await bot.add_cog(Rappel(bot))
