import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import re
import json
import os
import time
from discord.utils import get

class RP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminders_file = "reminders.json"
        self.load_reminders()

    def convert_duration(self, duration: str) -> int:
        """Convertit une durée au format libre en secondes."""
        duration = duration.lower()
        pattern = re.compile(r'(\d+)\s*(heures?|h|minutes?|m|min|secondes?|s|sec)')
        matches = pattern.findall(duration)
        if not matches:
            raise ValueError("Format de durée invalide.")
        
        total_seconds = 0
        for value, unit in matches:
            value = int(value)
            if unit.startswith('h'):
                total_seconds += value * 3600
            elif unit.startswith('m'):
                total_seconds += value * 60
            elif unit.startswith('s'):
                total_seconds += value
        
        return total_seconds

    def save_reminder(self, user_name, channel_id, duree, raison):
        """Sauvegarde un rappel dans le fichier JSON après avoir nettoyé les rappels expirés."""
        reminders = []
        if os.path.exists(self.reminders_file):
            with open(self.reminders_file, "r") as file:
                reminders = json.load(file)

        current_time = time.time()
        valid_reminders = []

        for reminder in reminders:
            created_at = reminder["created_at"]
            total_duration = self.convert_duration(reminder["duree"])
            elapsed_time = current_time - created_at
            remaining_time = total_duration - elapsed_time

            # Conserver uniquement les rappels encore valides
            if remaining_time > 0:
                valid_reminders.append(reminder)
            else:
                print(f"Rappel {reminder['raison']} pour {reminder['user_name']} supprimé car le temps est écoulé.")

        # Ajouter le nouveau rappel
        valid_reminders.append({
            "user_name": user_name,
            "channel_id": channel_id,
            "duree": duree,
            "raison": raison,
            "created_at": time.time()
        })

        # Sauvegarder les rappels mis à jour
        with open(self.reminders_file, "w") as file:
            json.dump(valid_reminders, file)

    def load_reminders(self):
        """Charge les rappels depuis le fichier JSON et les relance avec le temps restant."""
        if os.path.exists(self.reminders_file):
            with open(self.reminders_file, "r") as file:
                reminders = json.load(file)
        
        current_time = time.time()
        valid_reminders = []

        for reminder in reminders:
            user_name = reminder["user_name"]
            channel_id = reminder["channel_id"]
            duree = reminder["duree"]
            raison = reminder["raison"]
            created_at = reminder["created_at"]

            # Trouver l'utilisateur par nom
            user = get(self.bot.get_all_members(), name=user_name)
            channel = self.bot.get_channel(channel_id)

            if user and channel:
                # Calculer le temps écoulé
                elapsed_time = current_time - created_at
                total_duration = self.convert_duration(duree)
                remaining_time = total_duration - elapsed_time

                if remaining_time > 0:
                    # S'il reste du temps, planifier le rappel
                    valid_reminders.append(reminder)
                    asyncio.create_task(self.schedule_reminder(user, channel, remaining_time, raison))
                else:
                    # Si le rappel est déjà passé, le supprimer
                    print(f"Rappel de {raison} ignoré pour {user_name} car le temps est écoulé.")

        # Mettre à jour le fichier JSON avec uniquement les rappels encore valides
        with open(self.reminders_file, "w") as file:
            json.dump(valid_reminders, file)

    async def schedule_reminder(self, user, channel, seconds, raison):
        """Planifie un rappel après le nombre de secondes donné."""
        await asyncio.sleep(seconds)
        embed_rappel = discord.Embed(
            title="⏰ Rappel !",
            description=f"👋🏻 Hey {user.mention} !\n---------------------------\n⏰ Tu m'as demandé de te rappeler ceci : '{raison}' !",
            color=discord.Color.blue()
        )
        await channel.send(content=f"{user.mention}", embed=embed_rappel)

        # Supprimer le rappel après l'avoir exécuté
        self.delete_reminder(user.name, channel.id, raison)

    def delete_reminder(self, user_name, channel_id, raison):
        """Supprime un rappel spécifique du fichier JSON."""
        try:
            # Chargement des rappels existants
            with open(self.reminders_file, "r") as file:
                reminders = json.load(file)

            # Filtrage des rappels pour supprimer celui qui correspond aux critères
            reminders = [
                reminder for reminder in reminders
                if not (reminder["user_name"] == user_name and reminder["channel_id"] == channel_id 
                        and reminder["raison"] == raison)
            ]

            # Sauvegarde des rappels mis à jour
            with open(self.reminders_file, "w") as file:
                json.dump(reminders, file, indent=4)
                
        except FileNotFoundError:
            print("Fichier reminders.json introuvable.")
        except json.JSONDecodeError:
            print("Erreur de décodage du fichier reminders.json.")

    @app_commands.command(name="rp", description="Crée un rappel personnalisé.")
    @app_commands.describe(
        duree="Durée avant le rappel (par exemple: '1h', '5m', '30s', '1h05m', '1h05m30s' ).",
        raison="Raison du rappel (par exemple: 'Altération, Bonus, etc...')."
    )
    async def rp(self, interaction: discord.Interaction, duree: str, raison: str = None):
        user = interaction.user
        # Vérification des rôles
        if not any(role.name in ['role1', 'role2'] for role in user.roles): #Vérifie que l'utilisateur a l'un des rôles spécifiés (Les rôles doivent être écrit comme ceci : 'Role1', 'Role2' ect)
            await interaction.response.send_message(
                f"{user.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.", ephemeral=True)
            return
        try:
            # Convertir la durée en secondes
            seconds = self.convert_duration(duree)

            # Différer la réponse initiale
            await interaction.response.defer()

            # Si aucune raison n'est fournie, définir un message par défaut
            if raison is None:
                raison = "Aucune raison spécifiée."

            # Message de confirmation
            embed_confirmation = discord.Embed(
                title="⏰ Confirmation de l'ajout du rappel",
                description=f"Ton rappel dans {duree} pour '{raison}' est activé !",
                color=discord.Color.blue()
            )

            # Envoyer le message de confirmation
            await interaction.followup.send(embed=embed_confirmation)

            # Sauvegarder le rappel
            self.save_reminder(user.name, interaction.channel.id, duree, raison)

            # Attendre la durée spécifiée et envoyer le rappel
            await self.schedule_reminder(user, interaction.channel, seconds, raison)

        except ValueError:
            # Envoyer un message d'erreur sans différer la réponse
            await interaction.response.send_message("Erreur de format. Utilisez des durées comme '1h', '5m', '30s', '1h05m', '1h05m30s'.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(RP(bot))
