import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

class Sorciere(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='sorcière', description="Affiche l'aide pour l'event de la sorcière")
    async def sorciere(self, interaction: discord.Interaction):
        user = interaction.user
            # Vérification des rôles
        if not any(role.name in ['role1', 'role2'] for role in user.roles): #Vérifie que l'utilisateur a l'un des rôles spécifiés (Les rôles doivent être écrit comme ceci : 'Role1', 'Role2' ect)
            await interaction.response.send_message(
                f"{user.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.", ephemeral=True)
            return
        embed = discord.Embed(
            color=0x00ff00,
            title="🧙🏼‍♀️ -Deux choix s'offrent à vous :",
            description=(
                "🍱 -Ajouter un ingrédient\n"
                "ou\n"
                "🫳🏻-Faire une action"
            )
        )

        view = self.create_pagination_view_sorciere(with_close_button=True)
        await interaction.response.send_message(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.component:
            custom_id = interaction.data['custom_id']

            if custom_id == 'close':
                # Suppression du message lorsque le bouton Fermer est cliqué
                await interaction.response.defer()
                await interaction.message.delete()

            elif custom_id == 'sorciere01':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🍱 -Ingrédients :',
                    description=(
                        "🦇 Ajouter une chauve-souris:\n"
                        "60% ➡️ potion de temps ou de vitesse - ☄️ ou 💫\n"
                        "▬\n"
                        "🍺 Ajouter de la bière:\n"
                        "37,5% ➡️ 🤪 4H (mission boire de l'alcool validée)\n"
                        "▬\n"
                        "🩸 Ajouter du sang:\n"
                        "37,5% ➡️ potion de vie - max ☄️\n"
                        "▬\n"
                        "🕸️ Ajouter une toile d'araignée:\n"
                        "15% ➡️ 💔\n"
                        "▬\n"
                        "👁️ Ajouter un œil:\n"
                        "45% ➡️ potion de temps - ☄️ à ⭐\n"
                        "▬\n"
                        "🐸 Ajouter une grenouille:\n"
                        "45% ➡️ potion de temps ou de vitesse - ☄️\n"
                        "▬\n"
                        "🍏 Ajouter une pomme verte:\n"
                        "30% ➡️ potion de vie - max 🔥\n"
                        "45% ➡️ 💔\n"
                        "▬\n"
                        "🍎 Ajouter une pomme rouge:\n"
                        "15% ➡️ potion de vie 🟧\n"
                        "▬\n"
                        "🫀 Ajouter un cœur:\n"
                        "75% ➡️ Potion de vie - max 🌟\n"
                        "▬\n"
                        "🍄 Ajouter un champignon:\n"
                        "37,5% ➡️ potion de vie - max 🔥\n"
                        "37,5% ➡️ 💔\n"
                        "▬\n"
                        "🐀 Ajouter un rat:\n"
                        "30% ➡️ potion d'attaque - 🟧\n"
                        "22,5% ➡️ 💔\n"
                        "▬\n"
                        "🌹 Ajouter une rose:\n"
                        "30% ➡️ potion de soin - max 🔥\n"
                        "15% ➡️ 💔\n"
                        "▬\n"
                        "🦂 Ajouter un scorpion:\n"
                        "52,5% ➡️ potion d'attaque - max ☄️\n"
                        "7,5% ➡️ 🤕\n"
                        "▬\n"
                        "📦 Ajouter un ingrédient mystère:\n"
                        "67,5% ➡️ potion - max 🌟\n"
                        "7,5% ➡️ 🤢\n"
                        "▬\n"
                        "🐍 Ajouter un serpent:\n"
                        "45% ➡️ potion d'attaque - max ☄️\n"
                        "▬\n"
                        "🕷️ Ajouter une araignée:\n"
                        "22,5% ➡️ potion d'attaque - 🟧\n"
                        "▬\n"
                        "🦷 Ajouter une dent:\n"
                        "52,5% ➡️ potion d'attaque - max 💫\n"
                        "22,5% ➡️ 💔\n"
                        "▬\n"
                        "🧪 Ajouter un tube à essai:\n"
                        "37,5% ➡️ potion - max 💫\n"
                        "▬\n"
                        "🐢 Ajouter une tortue:\n"
                        "60% ➡️ potion de défense - max 💫\n"
                        "▬\n"
                        "🥀 Ajouter une rose fanée:\n"
                        "30% ➡️ potion de défense - max 🔥\n"
                        "15% ➡️ 💔\n"
                        "▬\n"
                        "🐔 Ajouter un poulet:\n"
                        "45% ➡️ potion d'énergie - max ⭐\n"
                        "7,5% ➡️ 💔\n"
                        "▬\n"
                        "🦴 Ajouter un os:\n"
                        "45% ➡️ potion d'énergie - max ⭐\n"
                        "7,5% ➡️ 💔\n"
                        "▬\n"
                        "🪱 Ajouter un ver:\n"
                        "45% ➡️ potion d'énergie - max 💫\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix :\n"
                        "🍱 - Ingrédients\n"
                        "🫳🏻 - Actions"
                    )
                )

                view = self.create_pagination_view_sorciere()
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'sorciere02':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🫳🏻 - Actions :',
                    description=(
                        "🔮 Réciter une formule magique:\n"
                        "37,5% ➡️ 😱\n"
                        "37,5% ➡️ potion de temps - ☄️\n"
                        "▬\n"
                        "⚗️ Distiller la potion:\n"
                        "🕙 55min\n"
                        "➡️ potion de temps - ☄️ à 🌟\n"
                        "▬\n"
                        "❄️ Laisser refroidir la potion:\n"
                        "30% ➡️ potion de temps - ☄️ ou 💫\n"
                        "22,5% ➡️ 🥶\n"
                        "▬\n"
                        "📖 Prononcer une incantation du livre de sortilèges:\n"
                        "🕙 25min\n"
                        "➡️ potion - max 💫\n"
                        "▬\n"
                        "🕙 Laisser reposer la potion:\n"
                        "🕙 45min\n"
                        "15% ➡️ potion sans effet\n"
                        "▬\n"
                        "🔥 Faire bouiller longuement la potion:\n"
                        "🕙 30min\n"
                        "45% ➡️ potion d'attaque - ⭐ à 💎\n"
                        "▬\n"
                        "⌛ Laisser la potion reposer un tout petit peu:\n"
                        "🕙 15min\n"
                        "▬\n"
                        "🌡️ Réchauffer un petit peu la marmite:\n"
                        "🕙 15min\n"
                        "60% ➡️ potion d'attaque - max 💫\n"
                        "7,5% ➡️ 💔\n"
                        "▬\n"
                        "🥄 Mélanger la potion:\n"
                        "🕙 5min\n"
                        "15% ➡️ potion - max ☄️\n"
                        "▬\n"
                        "🪄 Jeter un sort:\n"
                        "🕙 50min\n"
                        "➡️ potion - ☄️ à ⭐\n"
                        "▬▬▬▬▬▬\n"
                        "Autres choix :\n"
                        "🍱 - Ingrédients\n"
                        "🫳🏻 - Actions"
                    )
                )

                view = self.create_pagination_view_sorciere()
                await interaction.response.edit_message(embed=embed, view=view)

    def create_pagination_view_sorciere(self, with_close_button=True):
        view = View()
        view.add_item(Button(style=discord.ButtonStyle.primary, label='🍱', custom_id='sorciere01'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='🫳🏻', custom_id='sorciere02'))
        if with_close_button:
            view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
        return view

async def setup(bot):
    await bot.add_cog(Sorciere(bot))
