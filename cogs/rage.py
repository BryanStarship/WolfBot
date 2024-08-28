import discord
from discord.ext import commands
from discord import app_commands

class Rage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='rage', description="Affiche l'aide pour obtenir de la rage")
    async def rage(self, interaction: discord.Interaction):
        user = interaction.user
            # Vérification des rôles
        if not any(role.name in ['role1', 'role2'] for role in user.roles): #Vérifie que l'utilisateur a l'un des rôles spécifiés (Les rôles doivent être écrit comme ceci : 'Role1', 'Role2' ect)
            await interaction.response.send_message(
                f"{user.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.", ephemeral=True)
            return
        embed = discord.Embed(
            title='🤬-Rage:',
            description=
            "🤛▮-Attaquer à gauche:\n"
            "75% de réussite.\n"
            "▬\n"
            "🤜▮-Attaquer à droite:\n"
            "75% de réussite.\n"
            "▬\n"
            "🥩▮-Appâter avec de la viande:\n"
            "fonctionne mieux si l'animal est carnivore.\n"
            "▬\n"
            "🥕▮-Appâter avec des légumes:\n"
            "fonctionne mieux si l'animal est herbivore.\n"
            "▬\n"
            "🚶▮-Ne rien faire:\n"
            "20% de réussite.\n"
            "▬\n"
            "👊▮-Coup de poing:\n"
            "fonctionne mieux avec beaucoup d'attaque.\n"
            "▬\n"
            "⚡▮-Concentrer l’énergie pour attaquer:\n"
            "fonctionne mieux si beaucoup d'énergie.\n"
            "▬\n"
            "🏟️▮-Appeler les membres de la guilde:\n"
            "fonctionne si la rareté du familier est inférieure ou égale au nombre de membres de la guilde sur l’île.\n"
            "▬\n"
            "💪▮-Intimider la créature:\n"
            "fonctionne mieux si le niveau du joueur est élevé.\n"
            "▬\n"
            "🔥▮-Concentrer la force et attaquer:\n"
            "fonctionne mieux si peu d'énergie.\n"
            "▬\n"
            "💀▮-Faire le mort:\n"
            "fonctionne mieux si la vie est faible.\n"
            "▬\n"
            "🙏▮-Prier dieu:\n"
            "fonctionne mieux si on a des objets sacrés dans l’inventaire (comme la sainte kyullière).\n"
            "▬\n"
            "🛡️▮-Se protéger:\n"
            "fonctionne mieux avec de la défense.\n"
            "▬\n"
            "😤▮-Provoquer l’animal:\n"
            "fonctionne mieux si on a une forte attaque par rapport à son niveau ou posséder l’arme « insultes ».\n"
            "▬\n"
            "🏃▮-Fuir:\n"
            "fonctionne mieux avec une vitesse élevée.\n"
            "▬\n"
            "😱▮-Crier:\n"
            "40% si le familier est un mâle, 60% si c’est une femelle.\n"
            "▬\n"
            "🐾 ▮-Faire appel à son familier:\n"
            "fonctionne mieux avec un familier rare (et si celui en face ne l’est pas).\n",
            color=discord.Color.blue()
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Rage(bot))
