import discord
from discord.ext import commands
from discord import app_commands
import os
import sys
import platform
import json

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="admin",
        description="Commandes d'administration du bot"
    )
    @app_commands.describe(action="Choisissez une action : redémarrer, arrêter, obtenir des infos, afficher les changelogs ou les rappels perso")
    @app_commands.choices(action=[
        discord.app_commands.Choice(name="Redémarrer", value="restart"),
        discord.app_commands.Choice(name="Arrêter", value="shutdown"),
        discord.app_commands.Choice(name="Infos", value="info"),
        discord.app_commands.Choice(name="Changelogs", value="changelogs"),
        discord.app_commands.Choice(name="Rappel Perso", value="rappel_perso")
    ])
    @app_commands.checks.has_any_role('role1', 'role2')  # Vérifie que l'utilisateur a l'un des rôles spécifiés (Les rôles doivent être écrit comme ceci : 'Role1', 'Role2' ect)
    async def admin(self, interaction: discord.Interaction, action: str):
        if action == "restart":
            await interaction.response.send_message("Redémarrage du bot...", ephemeral=False)
            print("Redémarrage du bot demandé par", interaction.user)
            await self.bot.close()  # Ferme le bot
            os.execv(sys.executable, ['python'] + sys.argv)  # Relance le script du bot

        elif action == "shutdown":
            await interaction.response.send_message("Arrêt du bot...", ephemeral=False)
            print("Arrêt du bot demandé par", interaction.user)
            await self.bot.close()  # Ferme le bot sans le relancer

        elif action == "info":
            embed = discord.Embed(
                title=f"Informations sur le bot {self.bot.user.name}",
                color=discord.Color.blue()
            )
            embed.add_field(name="Nom du bot", value=self.bot.user.name, inline=False)
            embed.add_field(name="ID du bot", value=self.bot.user.id, inline=False)
            embed.add_field(name="Version de Discord.py", value=discord.__version__, inline=False)
            embed.add_field(name="Version de Python", value=platform.python_version(), inline=False)
            embed.add_field(name="Système d'exploitation", value=platform.system(), inline=False)
            embed.add_field(name="Nombre de serveurs", value=len(self.bot.guilds), inline=False)

            await interaction.response.send_message(embed=embed, ephemeral=False)
            print(f"Infos du bot demandées par {interaction.user}")

        elif action == "changelogs":
            changelogs_text = (
                "**V1.0 :**\n"
                "- Création de WolfBot\n"
                "- Création des commandes /z, /rp, /issues, /sorcière, /régime, !r, !ping, /m, /rage\n\n"
                "**V2.0 :**\n"
                "- Passage du code de WolfBot à python\n"
                "- Changement d'hébergeur\n"
                "- Code refait à zéro\n"
                "- Code des commandes /z, /rp, /issues, /sorcière, /régime, !r, !ping, /m, /rage refait à 100%\n"
                "- Ajout de la possibilité d'indiquer une durée précise pour /rp\n"
                "- Réfection des menus des commandes /issues, /m et /régime\n"
                "- Ajout de plus de détails dans !ping\n"
                "- Ajout d'un message d'alerte de redémarrage du bot\n"
                "- Modifications mineures dans les textes des commandes /z, !r et /rp\n"
                "- Correction de bugs et amélioration de la stabilité\n\n"
                "**V2.1 :**\n"
                "- Retrait de l'obligation d'utiliser l'option \"raison\" de la commande /rp\n\n"
                "**V2.2 :**\n"
                "- Correction du bug \"L'application ne répond pas\" avec la commande /rp lorsqu'une mauvaise durée était indiquée\n"
                "- Correction d'erreurs dans les textes de la commande /issues\n\n"
                "**V2.3 :**\n"
                "- Ajout d'un système d'enregistrement des rappels de la commande /rp qui permet au bot d'exécuter les rappels même après un redémarrage\n\n"
                "**V2.4 :**\n"
                "- Modifications du système d'enregistrement des rappels de la commande /rp\n"
                "- Ajout de la commande \"/admin\", réservée uniquement aux Administrateurs"
            )
            
            embed = discord.Embed(
                title="📜 Changelogs WolfBot",
                description=changelogs_text,
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed, ephemeral=False)
            print(f"Changelogs du bot demandés par {interaction.user}")

        elif action == "rappel_perso":
            try:
                # Lire les rappels depuis le fichier JSON
                with open("reminders.json", "r") as file:
                    reminders = json.load(file)

                if not reminders:
                    await interaction.response.send_message("Aucun rappel perso trouvé.", ephemeral=False)
                    return

                # Créer un embed pour afficher les rappels
                embed = discord.Embed(
                    title="📋 Rappels Personnalisés",
                    color=discord.Color.orange()
                )

                for reminder in reminders:
                    user_name = reminder["user_name"]
                    duree = reminder["duree"]
                    raison = reminder["raison"]
                    created_at = reminder["created_at"]

                    embed.add_field(
                        name=f"Rappel pour {user_name}",
                        value=f"Durée : {duree}\nRaison : {raison}\nCréé le : <t:{int(created_at)}:f>",
                        inline=False
                    )

                await interaction.response.send_message(embed=embed, ephemeral=False)
                print(f"Rappels perso demandés par {interaction.user}")

            except FileNotFoundError:
                await interaction.response.send_message("Le fichier reminders.json est introuvable.", ephemeral=True)
                print(f"Erreur: reminders.json introuvable.")
            except json.JSONDecodeError:
                await interaction.response.send_message("Erreur de lecture des rappels personnels.", ephemeral=True)
                print(f"Erreur de lecture du fichier reminders.json.")

    @admin.error
    async def admin_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.errors.MissingAnyRole):
            await interaction.response.send_message("Vous n'avez pas les rôles nécessaires pour utiliser cette commande.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Admin(bot))
