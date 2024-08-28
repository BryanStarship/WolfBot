import discord
from discord.ext import commands
from discord import app_commands

class Carte(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='carte', description='Affiche la carte du jeu avec les temps de trajets')
    async def carte(self, interaction: discord.Interaction):
        user = interaction.user
        # Vérification des rôles
        if not any(role.name in ['role1', 'role2'] for role in user.roles):#Vérifie que l'utilisateur a l'un des rôles spécifiés (Les rôles doivent être écrit comme ceci : 'Role1', 'Role2' ect)
            await interaction.response.send_message(
                f"{user.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.", ephemeral=True)
            return

        embed = discord.Embed(
            description="Voici la carte du jeu avec les temps de trajets :",
            color=discord.Color.blue()
        )

        # Chemin vers l'image locale
        file_path = "/home/container/carte.png"

        # Ouverture du fichier image
        with open(file_path, 'rb') as file:
            picture = discord.File(file, filename="carte.png")
            embed.set_image(url="attachment://carte.png")

            # Envoyer le message avec l'embed et l'image attachée
            await interaction.response.send_message(embed=embed, file=picture)

async def setup(bot):
    await bot.add_cog(Carte(bot))