import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import asyncio

class Issues(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='issues', description="Donne l'aide sur les issues selon un lieu précis")
    async def issues(self, interaction: discord.Interaction):
        user = interaction.user
            # Vérification des rôles
        if not any(role.name in ['role1', 'role2'] for role in user.roles): #Vérifie que l'utilisateur a l'un des rôles spécifiés (Les rôles doivent être écrit comme ceci : 'Role1', 'Role2' ect)
            await interaction.response.send_message(
                f"{user.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.", ephemeral=True)
            return
        embed = discord.Embed(
            color=0x00ff00,
            title='Voici le sommaire :',
            description=(
                "Page 1 :\n🌸-01-Le Berceau\n🌳-02-Bois Hurlant\n🛖-03-Boug-Coton\n🛣️-04-Chemin aux Loups\n🛣️-05-Chemin du Dédale\n▬▬\n"
                "Page 2 :\n🏘️-06-Claire De Ville\n🛣️-07-Croisement des Destins\n🏖️-08-La Dune\n🌸-09-L'Étendue\n🌳-10-Forêt Célestrum\n▬▬\n"
                "Page 3 :\n🌳-11-Forêt Du Vieillard\n🛣️-12-Grand Axe\n🛣️-13-Grande Rue\n🛶-14-Lac Mirage\n🏘️-15-Mergagnan\n▬▬\n"
                "Page 4 :\n⛰️-16-Mont Célestrum\n🏖️-17-Plage Sentinelle\n🛶-18-Rivière aux Crabes\n🏞️-19-Rivière Vacarme\n🛣️-20-Route des Merveilles\n▬▬\n"
                "Page 5 :\n🛣️-21-Route Grimpante\n🛣️-22-Route Marécageuse\n🏜️-23-Vallée des Rois\n🛖-24-Village Coco\n🏘️-25-Ville Forte\n▬▬\n"
                "Page 6 :\n🛣️-26-Voie champêtre\n🚢-27-Retour Bateau"
            )
        )
        
        view = self.create_pagination_view(with_close_button=True)
        await interaction.response.send_message(embed=embed, view=view)

    # Gestion des interactions
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.component:
            custom_id = interaction.data['custom_id']

            if custom_id == 'close':
                # Suppression du message lorsque le bouton Fermer est cliqué
                await interaction.response.defer()
                await interaction.message.delete()

            elif custom_id == 'back':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici le sommaire :',
                    description=(
                        "Page 1 :\n🌸-01-Le Berceau\n🌳-02-Bois Hurlant\n🛖-03-Boug-Coton\n🛣️-04-Chemin aux Loups\n🛣️-05-Chemin du Dédale\n▬▬\n"
                        "Page 2 :\n🏘️-06-Claire De Ville\n🛣️-07-Croisement des Destins\n🏖️-08-La Dune\n🌸-09-L'Étendue\n🌳-10-Forêt Célestrum\n▬▬\n"
                        "Page 3 :\n🌳-11-Forêt Du Vieillard\n🛣️-12-Grand Axe\n🛣️-13-Grande Rue\n🛶-14-Lac Mirage\n🏘️-15-Mergagnan\n▬▬\n"
                        "Page 4 :\n⛰️-16-Mont Célestrum\n🏖️-17-Plage Sentinelle\n🛶-18-Rivière aux Crabes\n🏞️-19-Rivière Vacarme\n🛣️-20-Route des Merveilles\n▬▬\n"
                        "Page 5 :\n🛣️-21-Route Grimpante\n🛣️-22-Route Marécageuse\n🏜️-23-Vallée des Rois\n🛖-24-Village Coco\n🏘️-25-Ville Forte\n▬▬\n"
                        "Page 6 :\n🛣️-26-Voie champêtre\n🚢-27-Retour Bateau"
                    )
                )
                view = self.create_pagination_view(with_close_button=True)
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id.startswith('page'):
                page = custom_id.replace('page', '')
                embed = self.create_page_embed(page)
                view = self.create_page_buttons(page, with_close_button=True)
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item01':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 👤-Paysan Fourche\n"
                        "ou\n"
                        "-02 🍎-Fermier Pommier"
                    )
                ).set_author(name="Lieu choisi : 🌸Le Berceau", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_berceau'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_berceau'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_berceau':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='👤-Paysan Fourche',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n"
                        "🔎-Aider le paysan à chercher sa fourche: :white_check_mark: (Risqué)\n"
                        "🕒 15m | ⭐ +125 | 💰 +25\n"
                        "Ou\n"
                        "🕒 30m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🤕 6h | 💔 -15\n"
                        "Ou\n"
                        "🕒 50m | ⭐ +25\n"
                        "▬▬\n"
                        "▶️-Passer son chemin:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🤕 6h | 💔 -15\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "-01 👤-Paysan Fourche\n"
                        "-02 🍎-Fermier Pommier"
                    )
                ).set_author(name="Lieu choisi : 🌸Le Berceau", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_berceau'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_berceau'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_berceau':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🍎-Fermier Pommier',
                    description=(
                        "🔚-End:\n"
                        "🕒 20m | ⭐ +15\n"
                        "Ou\n"
                        "❤️ +5 | ⭐ +350\n"
                        "▬▬\n"
                        "💶-Aller acheter des fruits à cet homme:\n"
                        "🤢 6h | 💔 -30 | 💸 -50\n"
                        "Ou\n"
                        "🕒 10m | ❤️ +5 | 💸 -50 | ⭐ +225\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n"
                        "👥-Aller voler des fruits dans l'arbre:\n"
                        "🕒 10m | ⭐ +125 | 💰 +150\n"
                        "Ou\n"
                        "🕒 15m | 💔 -25 | 💸 -50\n"
                        "Ou\n"
                        "🕒 15m | ❤️ +10 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25 | 💸 -50\n"
                        "▬▬\n"
                        "🏃-Ne pas s'en préoccuper: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "-01 👤-Paysan Fourche\n"
                        "-02 🍎-Fermier Pommier"
                    )
                ).set_author(name="Lieu choisi : 🌸Le Berceau", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_berceau'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_berceau'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item02':
                embed = discord.Embed(
                        color=0x00ff00,
                        title='Voici les issues possibles :',
                        description=(
                            "-01 ⁉️ - Inconnue\n"
                            "ou\n"
                            "-02 🚶🏼-Chariot"
                        )
                    ).set_author(name="Lieu choisi : 🌳Bois Hurlant", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_bois_hurlant'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_bois_hurlant'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)
            
            elif custom_id == '01_bois_hurlant':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='⁉️ - Inconnue',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "🕒 45m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🌳-Traverser quand même la forêt:\n"
                        "🕒 3h20m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 2h10m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🤕 6h | 💔 -20\n"
                        "▬▬\n\n"
                        "👈-Suivre les conseils de l'inconnue:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🤕 6h | 💔 -40\n"
                        "▬▬\n\n"
                        "👉-Éviter la forêt en partant du côté opposé à celui qu'on vous a indiqué:\n"
                        "🕒 2h20m | ⭐ +25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 ⁉️ - Inconnue\n"
                        "-02 🚶🏼-Chariot"
                    )
                ).set_author(name="Lieu choisi : 🌳Bois Hurlant")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_bois_hurlant'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_bois_hurlant'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_bois_hurlant':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🚶🏼-Chariot:',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🔨▮-Aider ces gens à réparer leur chariot:\n"
                        "🕒 45m | 💰 +75 | ⭐ +125\n"
                        "Ou\n"
                        "🕒 55m | 💔 -20 | 💸 -50\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +325 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🚶▮-Ne pas se préoccuper de ces individus vous semblant suspects:\n"
                        "⭐ 150\n"
                        "Ou\n"
                        "🤕 6h | 💔 -35\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 ⁉️ - Inconnue\n"
                        "-02 🚶🏼-Chariot"
                    )
                ).set_author(name="Lieu choisi : 🌳Bois Hurlant")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_bois_hurlant'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_bois_hurlant'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item03':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏘️ -Bijouterie/Auberge\n"
                        "ou\n"
                        "-02 🏘️ -Ménestrel\n"
                        "ou\n"
                        "-03 🧒-Enfants\n"
                        "ou\n"
                        "-04 ⚔️ -Seigneur\n"
                        "ou\n"
                        "-05 🦹-Silhouettes\n"
                    )
                ).set_author(name="Lieu choisi : 🛖Boug-Coton", icon_url="https://example.com/your-icon.png")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_boug_coton'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_boug_coton':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏘️ -Bijouterie/Auberge',
                    description=(
                        "🔚-End:\n"
                        "🕒 1h | ❤️ +20 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🗣️-Aller voir le bijoutier et discuter:\n"
                        "🕒 50m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 1h15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "💸-Essayer de voler le bijoutier:\n"
                        "⭐ +150 | 💰 +500\n"
                        "Ou\n"
                        "🕒 3h | ⭐ +\n"
                        "▬▬\n\n"
                        "🏡-Aller à l'auberge se reposer:\n"
                        "🕒 1h | ❤️ +20 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 30m | ❤️ +10 | ⭐ +225\n"
                        "Ou\n"
                        "💔 -15\n"
                        "▬▬\n\n"
                        "🚶-Continuer votre route: :white_check_mark:\n"
                        "❤️ +5 | ⭐ +350\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️-Bijouterie/Auberge\n"
                        "-02 🏘️-Ménestrel\n"
                        "-03 🧒-Enfants\n"
                        "-04 ⚔️-Seigneur\n"
                        "-05 🦹-Silhouettes"
                    )
                ).set_author(name="Lieu choisi : 🛖Boug-Coton")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_boug_coton'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_boug_coton':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏘️-Ménestrel',
                    description=(
                        "🔚-End:\n"
                        "⭐ 150\n"
                        "Ou\n"
                        "😖 40m | ⭐ +310 | 🔨 Item\n"
                        "Ou\n"
                        "🔒 24h\n"
                        "▬▬\n\n"
                        "🤪-Chanter un amour fou: :white_check_mark:\n"
                        "😱 10m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🥰-Chanter un amour terne et redondant:\n"
                        "🕒 6h | ⭐ +25\n"
                        "Ou\n"
                        "❤️ +20 | ⭐ +350\n"
                        "Ou\n"
                        "💸 -100 | ⭐ +150\n"
                        "▬▬\n\n"
                        "👑-Chanter sur la royauté et sur le pouvoir en place:\n"
                        "⭐ +250 | 💰 +600\n"
                        "Ou\n"
                        "🔒 24h\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🪕-Chanter sur le métier de ménestrel: :white_check_mark:\n"
                        "🕒 8h | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +300\n"
                        "▬▬\n\n"
                        "⚔️-Chanter sur notre vie, notre histoire héroïque:\n"
                        "🕒 5m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 8h | ⭐ +25\n"
                        "Ou\n"
                        "🤢 6h | 💰 +200 | 🔨 Item\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️-Bijouterie/Auberge\n"
                        "-02 🏘️-Ménestrel\n"
                        "-03 🧒-Enfants\n"
                        "-04 ⚔️-Seigneur\n"
                        "-05 🦹-Silhouettes"
                    )
                ).set_author(name="Lieu choisi : 🛖Boug-Coton")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_boug_coton'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '03_boug_coton':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🧒-Enfants',
                    description=(
                        "🔚-End:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -5\n"
                        "Ou\n"
                        "🕒 2h | ⭐ +25 | 💸 -100\n"
                        "▬▬\n\n"
                        "⚔️-Jouer à se battre:\n"
                        "🕒 20m | ⭐ +25 (×2)\n"
                        "Ou\n"
                        "💔 -1\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -250\n"
                        "▬▬\n\n"
                        "🏹-Leur apprendre à tirer à l'arc:\n"
                        "🤕 6h | 💔 -25\n"
                        "Ou\n"
                        "🕒 3h10m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "👥-Jouer au fuyard et au garde:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 5m | ⭐ +25\n"
                        "Ou\n"
                        "🤕 6h | 💔 -15\n"
                        "▬▬\n\n"
                        "❌-Refuser et passer votre chemin: :white_check_mark:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "🤕 6h\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️ -Bijouterie/Auberge\n"
                        "-02 🏘️-Ménestrel\n"
                        "-03 🧒-Enfants\n"
                        "-04 ⚔️-Seigneur\n"
                        "-05 🦹-Silhouettes"
                    )
                ).set_author(name="Lieu choisi : 🛖Boug-Coton")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_boug_coton'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '04_boug_coton':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='⚔️-Seigneur',
                    description=(
                        "🔚-End:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -200\n"
                        "Ou\n"
                        "❤️ +30 | ⭐ +350\n"
                        "▬▬\n\n"
                        "🤝-Proposer votre aide au seigneur de Boug-Coton:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "😵 12h | 💔 -105\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +300\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +500\n"
                        "Ou\n"
                        "🕒 5h | ⭐ +25\n"
                        "▬▬\n\n"
                        "👥-Assister au duel:\n"
                        "⭐ +150 (×3)\n"
                        "Ou\n"
                        "⭐ +250 | 💰 500\n"
                        "Ou\n"
                        "🤕 6h | 💔 -60\n"
                        "Ou\n"
                        "🤕 6h | 💔 -50\n"
                        "Ou\n"
                        "❤️ +20 | ⭐ +350\n"
                        "▬▬\n\n"
                        "🚶-Visiter Boug-Coton:\n"
                        "⭐ 150 (×2)\n"
                        "Ou\n"
                        "🤕 6h\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🪙-Organiser des paris: :white_check_mark:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +900\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -200\n"
                        "Ou\n"
                        "🤕 6h | 💔 -30\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +400\n"
                        "Ou\n"
                        "🤕 6h | 💔 -60\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +300\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️ -Bijouterie/Auberge\n"
                        "-02 🏘️-Ménestrel\n"
                        "-03 🧒-Enfants\n"
                        "-04 ⚔️-Seigneur\n"
                        "-05 🦹-Silhouettes"
                    )
                ).set_author(name="Lieu choisi : 🛖Boug-Coton")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_boug_coton'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '05_boug_coton':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🦹-Silhouettes',
                    description=(
                        "🔚-End\n"
                        "🕒 2h | ⭐ +25\n"
                        "Ou\n"
                        "🤪 4h | 💔 -5 | 💸 -75\n"
                        "Ou\n"
                        "💔 -30 | 💸 -100\n"
                        "Ou\n"
                        "🕒 10m | 💸 -50 | 🔨 Item\n"
                        "▬▬\n\n"
                        "⚔️-Affronter les silhouettes: :white_check_mark:\n"
                        "😖 40m | 💔 -20\n"
                        "Ou\n"
                        "🤢 6h\n"
                        "Ou\n"
                        "🕒 15m | 💰 +600 | ⭐ +125\n"
                        "Ou\n"
                        "🕒 45m | ⭐ +325 | 🔨 Item\n"
                        "▬▬\n\n"
                        "😈-Tenter de retrouver les silhouettes afin de les aider:\n"
                        "🕒 30m | 💸 -165\n"
                        "Ou\n"
                        "🕒 30m | ❤️ +15 | 💰 +165 | ⭐ +325\n"
                        "Ou\n"
                        "🕒 3h | ⭐ +25\n"
                        "Ou\n"
                        "🔒 24h\n"
                        "▬▬\n\n"
                        "🔊-Révéler à tous ce qu'il en est:\n"
                        "💔 -45 | 💸 -250\n"
                        "Ou\n"
                        "🕒 3h | 💰 +300 | ⭐ +125\n"
                        "Ou\n"
                        "🕒 1h | 💰 +450 | ⭐ +125\n"
                        "Ou\n"
                        "🕒 2h | ⭐ +25\n"
                        "▬▬\n\n"
                        "🏃-Partir d'ici rapidement:\n"
                        "⭐ +125\n"
                        "Ou\n"
                        "😖 40m | 💔 -20\n"
                        "Ou\n"
                        "😵 12h | 💔 -45\n"
                        "Ou\n"
                        "🕒 1h | ❤️ +50\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️-Bijouterie/Auberge\n"
                        "-02 🏘️-Ménestrel\n"
                        "-03 🧒-Enfants\n"
                        "-04 ⚔️-Seigneur\n"
                        "-05 🦹-Silhouettes"
                    )
                ).set_author(name="Lieu choisi : 🛖Boug-Coton")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_boug_coton'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_boug_coton'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item04':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏰-Duc Benatis\n"
                        "ou\n"
                        "-02 🌳-Arbre tombé"
                    )
                ).set_author(name="Lieu choisi : 🛣️Chemin aux Loups", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_chemin_loups'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_chemin_loups'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_chemin_loups':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏰-Duc Benatis',
                    description=(
                        "🔚-End:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -1\n"
                        "▬▬\n\n"
                        "🤴-Aller voir le duc:\n"
                        "🕒 50m | ❤️ +10 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 30m | ⭐ +125 | 💰 +150\n"
                        "Ou\n"
                        "🔒 24h\n"
                        "▬▬\n\n"
                        "🎉-Rester à la fête:\n"
                        "🕒 2h45m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 1h25m | ⭐ +25 | 💸 -100\n"
                        "Ou\n"
                        "🕒 1h | ❤️ +50 | ⭐ +225\n"
                        "▬▬\n\n"
                        "🎁-Lui offrir un cadeau: :white_check_mark:\n"
                        "💸 -400 | ⭐ +150\n"
                        "Ou\n"
                        "🕒 35m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🍌-Sortir pour aller lui voler des bananes dans son exploitation:\n"
                        "🔒 24h\n"
                        "Ou\n"
                        "❤️ +20 | ⭐ +350\n"
                        "Ou\n"
                        "🤢 6h\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏰-Duc Benatis\n"
                        "-02 🌳-Arbre tombé"
                    )
                ).set_author(name="Lieu choisi: 🛣️Chemin aux Loups", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_chemin_loups'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_chemin_loups'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_chemin_loups':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏰-Duc Benatis',
                    description=(
                        "🔚-End:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "🤕 6h | 💔 -20 | 💸 -150\n"
                        "▬▬\n\n"
                        "🪓-Couper l'arbre et continuer:\n"
                        "🕒 30m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 1h30m | 💸 -175\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🧗-Escalader l'arbre:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🤕 6h | 💔 -15\n"
                        "Ou\n"
                        "⭐ +50 | 💸 -250\n"
                        "▬▬\n\n"
                        "🚶-Passer par un autre chemin: :white_check_mark:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 3h | ⭐ +25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏰-Duc Benatis\n"
                        "-02 🌳-Arbre tombé"
                    )
                ).set_author(name="Lieu choisi: 🛣️Chemin aux Loups", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_chemin_loups'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_chemin_loups'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item05':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏇🏿-Chevalier noir\n"
                        "ou\n"
                        "-02 🧝‍♀️-Grotte femme"
                    )
                ).set_author(name="Lieu choisi: 🛣️Chemin du Dédale", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_chemin_dedale'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_chemin_dedale'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_chemin_dedale':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏇🏿-Chevalier noir',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🚶-Continuer votre route normalement:\n"
                        "💔 -45\n"
                        "Ou\n"
                        "❤️ +10 | ⭐ +350\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🌿-Se cacher dans un buisson au bord de la route:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -15\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "▬▬\n\n"
                        "👋-Lui faire signe pour qu'il s'arrête:\n"
                        "🕒 50m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -400\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏇🏿-Chevalier noir\n"
                        "-02 🧝‍♀️-Grotte femme"
                    )
                ).set_author(name="Lieu choisi : 🛣️Chemin du Dédale", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_chemin_dedale'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_chemin_dedale'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_chemin_dedale':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🧝‍♀️-Grotte femme',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ +550 | 💰 +500 | 🔨 Item\n"
                        "Ou\n"
                        "🤢 6h\n"
                        "▬▬\n\n"
                        "🏹-Vous empresser de l'aider:\n"
                        "🤢 6h | 💔 -70\n"
                        "Ou\n"
                        "🕒 1h30m | ⭐ +25 | 💸 -300\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +425 | 💰 +3000\n"
                        "Ou\n"
                        "🕒 10m | 💔 -35\n"
                        "▬▬\n\n"
                        "😎-Faire mine de vous éloigner pour revenir seul fouiller la grotte:\n"
                        "🕒 1h | ⭐ +25\n"
                        "Ou\n"
                        "🕒 1h | 💔 -10 | 💸 -200\n"
                        "Ou\n"
                        "🕒 1h | ❤️ +30 | ⭐ +325 | 💰 +600\n"
                        "Ou\n"
                        "🕒 30m | ❤️ +10 | ⭐ +225\n"
                        "▬▬\n\n"
                        "🥩-Lui demander l'auberge la plus proche:\n"
                        "🕒 4h | ⭐ +25 | 💸 -300\n"
                        "Ou\n"
                        "🕒 1h | ❤️ +15 | ⭐ +225 | 💸 -100\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏇🏿-Chevalier noir\n"
                        "-02 🧝‍♀️-Grotte femme"
                    )
                ).set_author(name="Lieu choisi : 🛣️Chemin du Dédale", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_chemin_dedale'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_chemin_dedale'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item06':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏘️ -Village\n"
                        "Ou\n"
                        "-02 🏙️-Groupe d'hommes\n"
                        "Ou\n"
                        "-03 👤-Garde Voleur\n"
                        "Ou\n"
                        "-04 👮-Prisonnier\n"
                        "Ou\n"
                        "-05 📚-Bibliothèque\n"
                        "Ou\n"
                        "-06 🏟️-Tournois seigneurial"
                    )
                ).set_author(name="Lieu choisi : 🏘️Claire De Ville", icon_url="https://example.com/your-icon.png")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_claire_ville'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='06', custom_id='06_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_claire_ville':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏘️ -Village',
                    description=(
                        "🔚-End:\n"
                        "🕒 3h20m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🏠-Aller à l'auberge:\n"
                        "🕒 2h | ⭐ +25\n"
                        "Ou\n"
                        "😴 3h | ⭐ +220 | 💸 -70 | ❤️ +15\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🔨-Aller à la forge: :white_check_mark:\n"
                        "⭐ 150 (×2)\n"
                        "Ou\n"
                        "🕒 40m | 💸 -300 | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🎪-Aller au marché:\n"
                        "🕒 30m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +25\n"
                        "Ou\n"
                        "🤕 12h | 💔 -60\n"
                        "▬▬\n\n"
                        "🚶-Repartir:\n"
                        "🕒 1h10m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 25m | ⭐ +25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️ -Village\n"
                        "-02 🏙️-Groupe d'hommes\n"
                        "-03 👤-Garde Voleur\n"
                        "-04 👮-Prisonnier\n"
                        "-05 📚-Bibliothèque\n"
                        "-06 🏟️-Tournois seigneurial"
                    )
                ).set_author(name="Lieu choisi : 🏘️Claire De Ville")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_claire_ville'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='06', custom_id='06_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_claire_ville':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🏙️-Groupe d'hommes",
                    description=(
                        "🔚-End:\n"
                        "🕒 35m | ⭐ +25\n"
                        "▬▬\n\n"
                        "👥-Tenter de commercer avec eux:\n"
                        "🕒 45m | 💸 -200 | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "💸 -70 | ⭐ +150\n"
                        "Ou\n"
                        "🕒 45m | 💸 -200 | ⭐ +25\n"
                        "▬▬\n\n"
                        "🏃-Continuer votre route sans perdre de temps: :white_check_mark:\n"
                        "⭐ +150 (×3)\n"
                        "Ou\n"
                        "😖 40m | 💔 -5\n"
                        "▬▬\n\n"
                        "💰-Prendre discrètement quelques pièces dans la caisse:\n"
                        "💰 +100 | ⭐ +250\n"
                        "Ou\n"
                        "🕒 30m | 💸 -200 | ⭐ +25\n"
                        "Ou\n"
                        "😖 40m | 💔 -20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️ -Village\n"
                        "-02 🏙️-Groupe d'hommes\n"
                        "-03 👤-Garde Voleur\n"
                        "-04 👮-Prisonnier\n"
                        "-05 📚-Bibliothèque\n"
                        "-06 🏟️-Tournois seigneurial"
                    )
                ).set_author(name="Lieu choisi : 🏘️Claire De Ville")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_claire_ville'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='06', custom_id='06_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '03_claire_ville':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="👤-Garde Voleur",
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ + 150\n"
                        "Ou\n"
                        "🕒 5m | ⭐ +25\n"
                        "▬▬\n\n"
                        "👊-Attaquer le garde par surprise dans l'optique d'aider la femme:\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🤕 6h | 💔 -55\n"
                        "Ou\n"
                        "🕒 30m | ⭐ +125 | 💰 +25\n"
                        "▬▬\n\n"
                        "🚶-Passer votre chemin:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -5\n"
                        "▬▬\n\n"
                        "🤙-Alerter d'autres gardes sur les agissements de leur collègue:\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🤕 6h | 💔 -35\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️ -Village\n"
                        "-02 🏙️-Groupe d'hommes\n"
                        "-03 👤-Garde Voleur\n"
                        "-04 👮-Prisonnier\n"
                        "-05 📚-Bibliothèque\n"
                        "-06 🏟️-Tournois seigneurial"
                    )
                ).set_author(name="Lieu choisi : 🏘️Claire De Ville")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_claire_ville'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='06', custom_id='06_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '04_claire_ville':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="👮-Prisonnier",
                    description=(
                        "🔚-End:\n"
                        "🕒 2h | ⭐ +25\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +15\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20\n"
                        "▬▬\n\n"
                        "🗣️-Tenter de vous expliquer:\n"
                        "🕒 3h | ⭐ +25\n"
                        "Ou\n"
                        "🕒 3h | ⭐ +125 | 💰 +75\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 15m | 💔 -10\n"
                        "▬▬\n\n"
                        "🕑-Attendre que quelque chose se passe:\n"
                        "🔒 24h\n"
                        "Ou\n"
                        "🕒 2h | ⭐ +25\n"
                        "Ou\n"
                        "❤️ +15 | ⭐ +350\n"
                        "▬▬\n\n"
                        "🔓-Tenter de s'évader:\n"
                        "🔒 24h\n"
                        "Ou\n"
                        "❤️ +5 | ⭐ +350\n"
                        "Ou\n"
                        "🕒 15m | 💔 -10\n"
                        "▬▬\n\n"
                        "🕵️-Tenter de soudoyer la personne qui vous surveille:\n"
                        "⭐ +150 | 💸 -150\n"
                        "Ou\n"
                        "🕒 45m | ❤️ +20 | ⭐ +225 | 💸 -250\n"
                        "Ou\n"
                        "🔒 24h | 💔 -5\n"
                        "Ou\n"
                        "🕒 2h | ⭐ +25\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20\n"
                        "▬▬\n\n"
                        "💀-Faire le mort : :white_check_mark:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "🕒 4h | ⭐ +25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️ -Village\n"
                        "-02 🏙️-Groupe d'hommes\n"
                        "-03 👤-Garde Voleur\n"
                        "-04 👮-Prisonnier\n"
                        "-05 📚-Bibliothèque\n"
                        "-06 🏟️-Tournois seigneurial"
                    )
                ).set_author(name="Lieu choisi : 🏘️Claire De Ville")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_claire_ville'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='06', custom_id='06_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '05_claire_ville':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="📚-Bibliothèque",
                    description=(
                        "🔚-End:\n"
                        "🕛 1h | ⭐ +25\n"
                        "Ou\n"
                        "🕛 10m | ⭐ +25\n"
                        "Ou\n"
                        "Rien\n"
                        "▬▬\n\n"
                        "📔-Tenter de voler un livre pour le revendre:\n"
                        "🕛 20m | ⭐ +25\n"
                        "Ou\n"
                        "💰 +100 | ⭐ +250\n"
                        "Ou\n"
                        "💸 -400 | ⭐ +150\n"
                        "▬▬\n\n"
                        "📖-Lire un livre:\n"
                        "🕛 1h | ♥ +27 | ⭐ +225\n"
                        "Ou\n"
                        "🕛 10m | ⭐ +25\n"
                        "Ou\n"
                        "🤢 6h\n"
                        "Ou\n"
                        "🕛 30m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🗓️-Regarder le calendrier:\n"
                        "🕛 3h10m | 💰 +700 | ⭐ +125\n"
                        "Ou\n"
                        "🕛 10m | ♥ +7 | ⭐ +225\n"
                        "Ou\n"
                        "🕛 2h | ⭐ +25\n"
                        "Ou\n"
                        "🤪 4h | 💰 +200\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️ -Village\n"
                        "-02 🏙️-Groupe d'hommes\n"
                        "-03 👤-Garde Voleur\n"
                        "-04 👮-Prisonnier\n"
                        "-05 📚-Bibliothèque\n"
                        "-06 🏟️-Tournois seigneurial"
                    )
                ).set_author(name="Lieu choisi : 🏘️Claire De Ville")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_claire_ville'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='06', custom_id='06_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '06_claire_ville':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🏟️-Tournois seigneurial",
                    description=(
                        "🔚-End:\n"
                        "🕛 3h | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🐴-Participer à l'épreuve de joute:\n"
                        "🕛 1h55m | 💰 + 425 | ⭐ +125\n"
                        "Ou\n"
                        "🕛 2h40m | 💰 +565 | ⭐ +425 | 🔨 Item\n"
                        "Ou\n"
                        "💔 -45\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🎯-Participer à l'épreuve de tir à l'arc:\n"
                        "🕛 1h | 💰 +235 | ⭐ +125\n"
                        "Ou\n"
                        "🕛 1h | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "📜-Participer à l'épreuve de poésie:\n"
                        "💰 +120 | ⭐ +250\n"
                        "Ou\n"
                        "💸 -350\n"
                        "Ou\n"
                        "🕛 15m | ⭐ +325 | 🔨 Item\n"
                        "▬▬\n\n"
                        "⚔️-Participer à l'épreuve de combat à pied:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕛 2h | 💰 +320 | ⭐ +425 | 🔨 Item\n"
                        "Ou\n"
                        "😴 3h | ❤️ +10\n"
                        "▬▬\n\n"
                        "🍴-Changer d'avis et partir en quête d'un stand de nourriture:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "❤️ +15 | ⭐ +350\n"
                        "Ou\n"
                        "❤️ +10 | ⭐ +350\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏘️ -Village\n"
                        "-02 🏙️-Groupe d'hommes\n"
                        "-03 👤-Garde Voleur\n"
                        "-04 👮-Prisonnier\n"
                        "-05 📚-Bibliothèque\n"
                        "-06 🏟️-Tournois seigneurial"
                    )
                ).set_author(name="Lieu choisi : 🏘️Claire De Ville")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='05', custom_id='05_claire_ville'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='06', custom_id='06_claire_ville'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item07':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🦊- Renard\n"
                        "ou\n"
                        "-02 🔎 - Guerre survivants"
                    )
                ).set_author(name="Lieu choisi : 🛣️Croisement des Destins", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_croisement_destins'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_croisement_destins'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_croisement_destins':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🦊- Renard',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "🕒 10m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🍽️-Tenter de cuisiner le renard:\n"
                        "🤢 6h\n"
                        "Ou\n"
                        "🕒 40m | ⭐ +25\n"
                        "Ou\n"
                        "💔 -20\n"
                        "Ou\n"
                        "🕒 40m | ❤️ +20 | ⭐ +225\n"
                        "▬▬\n\n"
                        "🚶-Ignorer simplement cela et vous dépêcher de rejoindre l'auberge la plus proche:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -20\n"
                        "▬▬\n\n"
                        "🔪-Dépecer le renard pour revendre sa peau:\n"
                        "🕒 1h30m | ⭐ +125 | 💰 +500\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🤢 6h\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🦊- Renard\n"
                        "-02 🔎 - Guerre survivants"
                    )
                ).set_author(name="Lieu choisi: 🛣️Croisement des Destins", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_croisement_destins'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_croisement_destins'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_croisement_destins':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🔎 - Guerre survivants',
                    description=(
                        "🔚 -End:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "😴 3h | 💔 -25\n"
                        "▬▬\n\n"
                        "🤝-Proposer son aide:\n"
                        "🕒 45m | ⭐ +125 | 💰 +100\n"
                        "Ou\n"
                        "🕒 15m | 💔 -10 | 💸 -30\n"
                        "▬▬\n\n"
                        "🕵️-Piller les corps: :white_check_mark:\n"
                        "🕒 15m | ⭐ +125 | 💰 +50\n"
                        "Ou\n"
                        "🕒 25m | ⭐ +25 | 💸 -100\n"
                        "▬▬\n\n"
                        "🚶-Ne pas les aider:\n"
                        "🕒 30m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🤕 6h | 💔 -15\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🦊- Renard\n"
                        "-02 🔎 - Guerre survivants"
                    )
                ).set_author(name="Lieu choisi: 🛣️Croisement des Destins", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_croisement_destins'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_croisement_destins'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item08':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🌡️-Température\n"
                        "ou\n"
                        "-02 🏜️ -Souterrain"
                    )
                ).set_author(name="Lieu choisi : 🏖️La Dune", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_dune'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_dune'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_dune':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🌡️-Température',
                    description=(
                        "🔚-End:\n"
                        "💔 -20\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🔍-Chercher un point d'eau aux alentours: :white_check_mark:\n"
                        "🕒 50m | ❤️ +10 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 30m | ❤️ +10 | ⭐ +525 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 3h | 💔 -10\n"
                        "▬▬\n\n"
                        "🌳-Se reposer au pied d'un arbre:\n"
                        "🕒 55m | ❤️ +10 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +25 | 💸 -100\n"
                        "▬▬\n\n"
                        "😴-Se reposer sur place:\n"
                        "🕒 3h | ⭐ +25\n"
                        "Ou\n"
                        "🕒 1h30 | ❤️ +1 | ⭐ +225\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🌡️-Température\n"
                        "-02 🏜️ -Souterrain"
                    )
                ).set_author(name="Lieu choisi : 🏖️La Dune", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_dune'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_dune'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_dune':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏜️ -Souterrain',
                    description=(
                        "🔚-End:\n"
                        "😴 3h\n"
                        "Ou\n"
                        "🕛 3h | ⭐ +25\n"
                        "Ou\n"
                        "😵‍💫 12h | 💔 -45\n"
                        "▬▬\n\n"
                        "🔍-Explorer le souterrain:\n"
                        "🚶🏻‍♂️ Rien\n"
                        "Ou\n"
                        "🕛 20m | 💰 +785 | ⭐ +525 | 🔨 Item\n"
                        "Ou\n"
                        "🕛 25m | 💔 -20 | 💰+165\n"
                        "Ou\n"
                        "🧐 4h30m (×2)\n"
                        "Ou\n"
                        "💔 -15\n"
                        "▬▬\n\n"
                        "🚶-Poursuivre votre chemin:\n"
                        "🕛 30m | ❤️ +5 | ⭐ +225\n"
                        "Ou\n"
                        "🚶🏻‍♂️ Rien\n"
                        "Ou\n"
                        "😴 3h\n"
                        "Ou\n"
                        "💔 -25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🌡️-Température\n"
                        "-02 🏜️ -Souterrain"
                    )
                ).set_author(name="Lieu choisi : 🏖️La Dune", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_dune'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_dune'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item09':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏠-Ouvrier\n"
                        "ou\n"
                        "-02 🌾-Fourche préférée"
                    )
                ).set_author(name="Lieu choisi : 🌸L'Étendue", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_etendue'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_etendue'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_etendue':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏠-Ouvrier',
                    description=(
                        "🔚-End:\n"
                        "🕒 30m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🔨-Discuter avec l'ouvrier:\n"
                        "🕒 1h | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "🤕 12h | 💔 -70\n"
                        "▬▬\n\n"
                        "🛏️-Demander à rester là durant la nuit pour vous reposer et reprendre des forces: :white_check_mark:\n"
                        "😴 3h | ❤️ +10 | ⭐ +220\n"
                        "Ou\n"
                        "🕒 5m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 1h40m | ❤️ +5 | ⭐ +225\n"
                        "▬▬\n\n"
                        "🚶-Pas de temps à perdre ! Il faut continuer votre route !:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +25\n"
                        "Ou\n"
                        "😴 3h | 💔 -20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏠-Ouvrier\n"
                        "-02 🌾-Fourche préférée"
                    )
                ).set_author(name="Lieu choisi : 🌸L'Étendue", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_etendue'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_etendue'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_etendue':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🌾-Fourche préférée',
                    description=(
                        "💔 -1\n"
                        "▬▬\n\n"
                        "🔚-End: :white_check_mark:\n"
                        "❤️ +10 | ⭐ +350\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🍀-Chercher près des pâturages:\n"
                        "🕒 20 | ⭐ +125 | 💰 +500\n"
                        "Ou\n"
                        "🕒 2h30m | ❤️ +30 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 20m | 💔 -10\n"
                        "▬▬\n\n"
                        "🍇-Chercher dans les vignes:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "🤪 4h | ❤️ +3\n"
                        "▬▬\n\n"
                        "🎑-Chercher dans le champ de blé: :white_check_mark:\n"
                        "🕒 30m | ⭐ +125 | 💰 +400\n"
                        "Ou\n"
                        "🕒 3h | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "❤️ +4 | ⭐ +350\n"
                        "▬▬\n\n"
                        "✖️-Refuser d'aider le paysan:\n"
                        "💔 -4\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "❤️ +10 | ⭐ +350\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏠-Ouvrier\n"
                        "-02 🌾-Fourche préférée"
                    )
                ).set_author(name="Lieu choisi : 🌸L'Étendue", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_etendue'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_etendue'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item10':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🍽️-Grotte repas\n"
                        "ou\n"
                        "-02 🌲-Ermite"
                    )
                ).set_author(name="Lieu choisi : 🌳Forêt Célestrum", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_foret_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_foret_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_foret_celestrum':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🍽️-Grotte repas',
                    description=(
                        "🔚-End:\n"
                        "🕒 4h30m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🔦-Entrer plus profondément dans la grotte:\n"
                        "🕒 3h20m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "😖 40m | 💔 -1\n"
                        "▬▬\n\n"
                        "🏃-Continuer votre route, pas de temps à perdre !: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🔍-Fouiller les alentours:\n"
                        "🕒 30m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -190\n"
                        "Ou\n"
                        "😖 40m | 💔 -25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🍽️-Grotte repas\n"
                        "-02 🌲-Ermite"
                    )
                ).set_author(name="Lieu choisi : 🌳Forêt Célestrum", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_foret_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_foret_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_foret_celestrum':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🌲-Ermite',
                    description=(
                        "🔚-End\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "🤢 6h\n"
                        "▬▬\n\n"
                        "🔎-S'introduire dans la maison:\n"
                        "💰 +350 | ⭐ +250\n"
                        "Ou\n"
                        "🤕 6h | 💔 -30\n"
                        "Ou\n"
                        "🕒 40m | ❤️ +40 | ⭐ +225\n"
                        "▬▬\n\n"
                        "🗣️-Demander des conseils à l'ermite:\n"
                        "🕒 5h | ⭐ +25\n"
                        "Ou\n"
                        "🕒 30m | ❤️ +25 | ⭐ +225\n"
                        "Ou\n"
                        "🤪 4h\n"
                        "▬▬\n\n"
                        "🚶-Repartir par là d'où vous venez: :white_check_mark:\n"
                        "⭐ +250 | 💰 +150\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -250\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🍽️-Grotte repas\n"
                        "-02 🌲-Ermite"
                    )
                ).set_author(name="Lieu choisi : 🌳Forêt Célestrum", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_foret_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_foret_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item11':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🌳-Arbre tombé\n"
                        "ou\n"
                        "-02 🩸-Homme blessé\n"
                        "ou\n"
                        "-03 🧚‍♀️-Fée Donia"
                    )
                ).set_author(name="Lieu choisi : 🌳Forêt Du Vieillard", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_foret_vieillard':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🌳-Arbre tombé',
                    description=(
                        "🔚-End:\n"
                        "🕒 1h40m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🪓-Couper l'arbre et continuer: :white_check_mark:\n"
                        "🕒 30m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🚶-Passer par un autre chemin:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 30m | 💔 -5\n"
                        "Ou\n"
                        "😖 40m | 💔 -25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🌳-Arbre tombé\n"
                        "-02 🩸-Homme blessé\n"
                        "-03 🧚‍♀️-Fée Donia"
                    )
                ).set_author(name="Lieu choisi : 🌳Forêt Du Vieillard", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_foret_vieillard':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🩸-Homme blessé',
                    description=(
                        "🔚-End:\n"
                        "⭐ +250 | 💰 +200\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -200\n"
                        "▬▬\n\n"
                        "💉-Aller chercher de quoi soigner l'homme blessé:\n"
                        "⭐ +250 | 💰 +400\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -200\n"
                        "Ou\n"
                        "💔 -15 | 💰 +300 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🔪-Achever l'homme pour récupérer son équipement: :white_check_mark:\n"
                        "💔 -10\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "⭐ +550 | 💰 +700 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🗣️-Crier afin d'alerter des gens:\n"
                        "⭐ +250 | 💰 +200\n"
                        "Ou\n"
                        "💔 -20\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 1h | ❤️ +20 | ⭐ +225\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🌳-Arbre tombé\n"
                        "-02 🩸-Homme blessé\n"
                        "-03 🧚‍♀️-Fée Donia"
                    )
                ).set_author(name="Lieu choisi : 🌳Forêt Du Vieillard", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '03_foret_vieillard':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🧚‍♀️-Fée Donia',
                    description=(
                        "🔚-End:\n"
                        "🕛 2h15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "👍-Accepter son offre:\n"
                        "🧍 Rien (×2)\n"
                        "Ou\n"
                        "😴 3h | ❤️ +35 | ⭐ +220\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "👿-Refuser:\n"
                        "🤕 6h | 💔 -25\n"
                        "Ou\n"
                        "🤢 6h | 💔 -10\n"
                        "▬▬\n\n"
                        "🤝-Trouver un compromis:\n"
                        "🧍 Rien\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🌳-Arbre tombé\n"
                        "-02 🩸-Homme blessé\n"
                        "-03 🧚‍♀️-Fée Donia"
                    )
                ).set_author(name="Lieu choisi : 🌳Forêt Du Vieillard", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_foret_vieillard'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item12':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🍲-Affamé\n"
                        "ou\n"
                        "-02 🌕-Créature"
                    )
                ).set_author(name="Lieu choisi : 🛣️Grand Axe", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_grand_axe'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_grand_axe'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_grand_axe':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🍲-Affamé',
                    description=(
                        "🔚-End:\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 4h20m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🍎-Escalader l'immense arbre qui vous fait face afin d'en récupérer les fruits:\n"
                        "❤️ +15 | ⭐ +350\n"
                        "Ou\n"
                        "😖 40m | 💔 -10\n"
                        "Ou\n"
                        "🤢 6h | 💔 -15\n"
                        "▬▬\n\n"
                        "🍄-Cueillir les champignons:\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 55m | ⭐ +25\n"
                        "Ou\n"
                        "😵 12h | 💔 -40\n"
                        "▬▬\n\n"
                        "🥗-Concocter une salade avec les plantes que vous trouvez: :white_check_mark:\n"
                        "❤️ +5 | ⭐ +350\n"
                        "Ou\n"
                        "🤤 1h20m | ⭐ +20\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🦌-Tenter de chasser un animal sauvage:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "😵 12h | 💔 -60\n"
                        "Ou\n"
                        "❤️ +20 | ⭐ +350\n"
                        "▬▬\n\n"
                        "🚶-Abandonner l'idée de manger ici et repartir dans l'espoir de trouver un meilleur lieu pour vous repaître:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🍲-Affamé\n"
                        "-02 🌕-Créature"
                    )
                ).set_author(name="Lieu choisi : 🛣️Grand Axe", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_grand_axe'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_grand_axe'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_grand_axe':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🌕-Créature',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 10m | 💔 -5\n"
                        "▬▬\n\n"
                        "⬆️-Continuer votre route:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 3h30m | ❤️ +30 | 💸 -200 | ⭐ +225\n"
                        "▬▬\n\n"
                        "⬇️-Faire demi tour:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -5\n"
                        "▬▬\n\n"
                        "⚔️-Affronter la créature: :white_check_mark:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "🕒 30m | ⭐ +25\n"
                        "▬▬\n\n"
                        "⛪-S'abriter dans une église Kyutiste:\n"
                        "😴 3h | ⭐ +20 (×2)\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 1h30m | ⭐ +25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🍲-Affamé\n"
                        "-02 🌕-Créature"
                    )
                ).set_author(name="Lieu choisi : 🛣️Grand Axe", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_grand_axe'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_grand_axe'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item13':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🐶-Chien\n"
                        "ou\n"
                        "-02 🚶-Marchand itinérant"
                    )
                ).set_author(name="Lieu choisi : 🛣️Grande Rue", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_grande_rue'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_grande_rue'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_grande_rue':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🐶-Chien',
                    description=(
                        "🔚-End:\n"
                        "💔 -10\n"
                        "▬▬\n\n"
                        "🐕▮-Suivre le chien: :white_check_mark:\n"
                        "🧐 4h30m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +176\n"
                        "▬▬\n\n"
                        "🏃-Continuer sans se préoccuper du chien:\n"
                        "🕒 15m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🤕 6h | 💔 -15\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🐶-Chien\n"
                        "-02 🚶-Marchand itinérant"
                    )
                ).set_author(name="Lieu choisi : 🛣️Grande Rue", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_grande_rue'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_grande_rue'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_grande_rue':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🚶-Marchand itinérant',
                    description=(
                        "🔚-End:\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 3h| ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 3h | ⭐ +25\n"
                        "▬▬\n\n"
                        "💸-Accepter de lui acheter un objet peu cher: :white_check_mark:\n"
                        "⭐ +450 | 💸 -100 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -100\n"
                        "▬▬\n\n"
                        "💰-Lui acheter un de ses plus chers objets:\n"
                        "⭐ +450 | 💸 -350 | 🔨 Item (×2)\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -350\n"
                        "▬▬\n\n"
                        "❌-Refuser:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🕵️-Voler sa marchandise:\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🤕 6h | 💔 -20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🐶-Chien\n"
                        "-02 🚶-Marchand itinérant"
                    )
                ).set_author(name="Lieu choisi : 🛣️Grande Rue", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_grande_rue'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_grande_rue'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item14':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🐟-Pêcheur\n"
                        "ou\n"
                        "-02 📬-Colis"
                    )
                ).set_author(name="Lieu choisi : 🛶Lac Mirage", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_lac_mirage'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_lac-mirage'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_lac_mirage':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🐟-Pêcheur',
                    description=(
                        "🔚-End:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🎣-Proposer son aide:\n"
                        "🕒 30m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 30m | ⭐ +125 | 💰 +234\n"
                        "Ou\n"
                        "😖 40m | 💔 -10\n"
                        "▬▬\n\n"
                        "🏃-Continuer votre route, pas de temps à perdre !: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🖐️-Pousser le pêcheur dans l'eau !:\n"
                        "⭐ +150 | 💸 -500\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🐟-Pêcheur\n"
                        "-02 📬-Colis"
                    )
                ).set_author(name="Lieu choisi : 🛶Lac Mirage", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_lac_mirage'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_lac_mirage'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_lac_mirage':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📬-Colis',
                    description=(
                        "🔚-End:\n"
                        "🕒 5m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150 (×2)\n"
                        "▬▬\n\n"
                        "✅-Accepter de livrer le colis:\n"
                        "🕒 15m | ⭐ +125 | 💰 +500\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +25 | 💸 -200\n"
                        "Ou\n"
                        "🕒 1h15m | ⭐ +325 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🕵️-Voler le colis: :white_check_mark:\n"
                        "⭐ +150 | 💸 -80\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +300\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +200\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "▬▬\n\n"
                        "❌-Refuser poliment:\n"
                        "🕒 15m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 30m | ❤️ +10 | ⭐ +225\n"
                        "Ou\n"
                        "💔 -10 | 🔨 Item\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🐟-Pêcheur\n"
                        "-02 📬-Colis"
                    )
                ).set_author(name="Lieu choisi : 🛶Lac Mirage", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_lac_mirage'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_lac_mirage'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item15':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🎆-Festival\n"
                        "ou\n"
                        "-02 🍻-Barman cobaye\n"
                        "ou\n"
                        "-03 👤-Price\n"
                        "ou\n"
                        "-04 🏚️-Chantier"
                    )
                ).set_author(name="Lieu choisi : 🏘️Mergagnan", icon_url="https://example.com/your-icon.png")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_mergagnan'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_mergagnan':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🎆-Festival',
                    description=(
                        "🔚-End:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 40m | ❤️ +5 | ⭐ +225\n"
                        "▬▬\n\n"
                        "🎯-Aller à un stand de jeu: :white_check_mark:\n"
                        "⭐ +150 | 💸 -200\n"
                        "Ou\n"
                        "🕒 30m | ⭐ +25\n"
                        "Ou\n"
                        "💰 +200 | ⭐ +250\n"
                        "▬▬\n\n"
                        "🎪-Aller à un stand de vente d'objets:\n"
                        "🕒 4h | ⭐ +25\n"
                        "Ou\n"
                        "💸 -200 | ⭐ +450 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🍢-Aller à un stand de nourriture:\n"
                        "🕒 30m | ❤️ +75 | 💸 -20 | ⭐ +225\n"
                        "Ou\n"
                        "🤢 6h | 💔 -100 | 💸 -20\n"
                        "Ou\n"
                        "💸 -20 | ⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🎆-Festival\n"
                        "-02 🍻-Barman cobaye\n"
                        "-03 👤-Price\n"
                        "-04 🏚️-Chantier"
                    )
                ).set_author(name="Lieu choisi : 🏘️Mergagnan")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_mergagnan'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_mergagnan':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🍻-Barman cobaye',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🍺-Accepter de servir de cobaye:\n"
                        "❤️ +30 | ⭐ +350\n"
                        "Ou\n"
                        "🤢 6h | 💰 +250\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "❌-Refuser sa proposition:\n"
                        "🕒 30m | ⭐ +25 | 💸 -50\n"
                        "Ou\n"
                        "⭐ +150 (×2)\n"
                        "▬▬\n\n"
                        "💰-Refuser, et tenter de voler des gens:\n"
                        "⭐ +250 | 💰 +1000\n"
                        "Ou\n"
                        "🔒 24h | 💸 -200\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🎆-Festival\n"
                        "-02 🍻-Barman cobaye\n"
                        "-03 👤-Price\n"
                        "-04 🏚️-Chantier"
                    )
                ).set_author(name="Lieu choisi : 🏘️Mergagnan")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_mergagnan'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '03_mergagnan':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='👤-Price',
                    description=(
                        "🔚-End:\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -300\n"
                        "▬▬\n\n"
                        "🚶-Le payer pour vous escorter jusqu'à votre prochaine destination: :white_check_mark:\n"
                        "⭐ +250 | 💰 +350\n"
                        "Ou\n"
                        "⭐ +550 | 💰 +150 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -100\n"
                        "Ou\n"
                        "🤕 6h | 💔 -20 | 💸 -300\n"
                        "▬▬\n\n"
                        "🍖-Faire connaissance autour d'un bon repas:\n"
                        "🕒 2h | ⭐ +25 | 💸 -150\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🤑-Tenter de lui voler de l'argent:\n"
                        "🤕 6h | 💔 -20\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🎆-Festival\n"
                        "-02 🍻-Barman cobaye\n"
                        "-03 👤-Price\n"
                        "-04 🏚️-Chantier"
                    )
                ).set_author(name="Lieu choisi : 🏘️Mergagnan")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_mergagnan'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '04_mergagnan':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏚️-Chantier',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "🕒 10m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🔎-Fouiller le chantier: :white_check_mark:\n"
                        "🕒 30m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 40m | ⭐ +425 | 🔨 Item\n"
                        "Ou\n"
                        "🤕 6h | 💔 -20\n"
                        "▬▬\n\n"
                        "⛓️-Fouiller les échafaudages:\n"
                        "🕒 45m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "😖 40m | 💔 -30\n"
                        "▬▬\n\n"
                        "🚶-Poursuivre votre voyage sans y prêter attention:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "😖 40m | 💔 -15\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🎆-Festival\n"
                        "-02 🍻-Barman cobaye\n"
                        "-03 👤-Price\n"
                        "-04 🏚️-Chantier"
                    )
                ).set_author(name="Lieu choisi : 🏘️Mergagnan")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mergagnan'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_mergagnan'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item16':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏔️-Ascension difficile\n"
                        "ou\n"
                        "-02 ⛰-Escalier\n"
                        "ou\n"
                        "-03 🌉-Pont délabré"
                    )
                ).set_author(name="Lieu choisi : ⛰️Mont Célestrum", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_mont_celestrum':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏔️-Ascension difficile',
                    description=(
                        "🔚-End:\n"
                        "😴 3h | ⭐ +20\n"
                        "▬▬\n\n"
                        "🌲-Continuer à travers la forêt de sapin: :white_check_mark:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🤕 6h | 💔 -25\n"
                        "▬▬\n\n"
                        "🏞️-Renoncer à grimper jusqu'en haut et rester proche des plaines:\n"
                        "🕒 2h30m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 2h30m | ❤️ +10 | ⭐ +255\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏔️-Ascension difficile\n"
                        "-02 ⛰-Escalier\n"
                        "-03 🌉-Pont délabré"
                    )
                ).set_author(name="Lieu choisi : ⛰️Mont Célestrum", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_mont_celestrum':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='⛰ -Escalier',
                    description=(
                        "🔚-End:\n"
                        "😴 3h | ❤️ +5 | ⭐ +220\n"
                        "Ou\n"
                        "🕒 10m | 💔 -10m\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🚶‍♂️-Faire demi-tour:\n"
                        "🕒 2h | ⭐ +125 | 💰 +200\n"
                        "Ou\n"
                        "💔 -30 | 💸 -120\n"
                        "Ou\n"
                        "🕒 1h | ❤️ +10 | ⭐ +225\n"
                        "▬▬\n\n"
                        "↗️-Emprunter l'escalier: :white_check_mark:\n"
                        "🕒 3h | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "😴 3h | ❤️ +15 | ⭐ +220\n"
                        "Ou\n"
                        "🕒 10m | 💔 -35\n"
                        "▬▬\n\n"
                        "🔎-Fouiller les alentours:\n"
                        "⭐ +250 | 💰 +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🤕 6h | 💔 -20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏔️-Ascension difficile\n"
                        "-02 ⛰-Escalier\n"
                        "-03 🌉-Pont délabré"
                    )
                ).set_author(name="Lieu choisi : ⛰️Mont Célestrum", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '03_mont_celestrum':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🌉-Pont délabré',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "🕒 20m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 5m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🌉-Prendre le risque d'emprunter ce pont:\n"
                        "🕒 5m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 10m | 💰 +50 | ⭐ +125\n"
                        "Ou\n"
                        "🤕 6h | 💔 -60\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🚶-Chercher un autre chemin un peu plus loin:\n"
                        "🕒 1h | ⭐ +25\n"
                        "Ou\n"
                        "🕒 45m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "😖 40m | ⭐ +10\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏔️-Ascension difficile\n"
                        "-02 ⛰ -Escalier\n"
                        "-03 🌉 -Pont délabré"
                    )
                ).set_author(name="Lieu choisi : ⛰️Mont Célestrum", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_mont_celestrum'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item17':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏖️ -Bernard l'hermite\n"
                        "ou\n"
                        "-02 ⚗️-Gruffo"
                    )
                ).set_author(name="Lieu choisi : 🏖️Plage Sentinelle", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_plage_sentinelle'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_plage_sentinelle'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_plage_sentinelle':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🏖️ -Bernard l'hermite",
                    description=(
                        "🔚-End:\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 1h | 💔 -10\n"
                        "▬▬\n\n"
                        "🤝-L'aider et le remettre sur pattes: :white_check_mark:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -1\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +500\n"
                        "▬▬\n\n"
                        "💞-Le prendre avec vous:\n"
                        "💔 -5\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 2h | ⭐ +25\n"
                        "▬▬\n\n"
                        "🍖-Décider de le manger:\n"
                        "🤢 6h\n"
                        "Ou\n"
                        "❤️ +10 | ⭐ +350\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏖️ -Bernard l'hermite\n"
                        "-02 ⚗️-Gruffo"
                    )
                ).set_author(name="Lieu choisi : 🏖️Plage Sentinelle", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_plage_sentinelle'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_plage_sentinelle'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_plage_sentinelle':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="⚗️-Gruffo",
                    description=(
                        "🔚-End:\n"
                        "😖 40m | ⭐ +10\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -225\n"
                        "Ou\n"
                        "🕒 20m | ❤️ +5 | ⭐ +225\n"
                        "▬▬\n\n"
                        "❌-Refuser la proposition de Gruffo:\n"
                        "😴 3h | ❤️ +15 | ⭐ +225\n"
                        "Ou\n"
                        "😖 40m | ⭐ +10\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🍸-Boire une potion au hasard:\n"
                        "🤪 4h | 💰 +200\n"
                        "Ou\n"
                        "❤️ +10 | ⭐ +350\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +25\n"
                        "Ou\n"
                        "🥶 1h | 💔 -20\n"
                        "▬▬\n\n"
                        "⚫-Boire la potion noire:\n"
                        "😖 40m | 💔 -70\n"
                        "Ou\n"
                        "😴 3h | ⭐ +120 | 💰 +400\n"
                        "▬▬\n\n"
                        "🏖️-Ignorer l'alchimiste et aller profiter de la plage: :white_check_mark:\n"
                        "⭐ +150 | 💸 -100\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -3\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏖️ -Bernard l'hermite\n"
                        "-02 ⚗️-Gruffo"
                    )
                ).set_author(name="Lieu choisi : 🏖️Plage Sentinelle", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_plage_sentinelle'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_plage_sentinelle'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item18':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏰-Château abandonné\n"
                        "ou\n"
                        "-02 🚶-Chemin rivière"
                    )
                ).set_author(name="Lieu choisi : 🛶Rivière aux Crabes", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_riviere_crabes'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_riviere_crabes'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_riviere_crabes':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🏰-Château abandonné",
                    description=(
                        "🔚-End:\n"
                        "🕒 15m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 30m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🔎-Entrer pour fouiller le château:\n"
                        "🤕 6h | 💔 -35\n"
                        "Ou\n"
                        "🕒 25m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25\n"
                        "▬▬\n\n"
                        "➡️-Continuer votre route: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🔁-Faire le tour du château par l'extérieur:\n"
                        "🕒 1h20m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 1h20m | ⭐ +225 | 💰 +450\n"
                        "Ou\n"
                        "🤕 6h | 💔 -20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏰-Château abandonné\n"
                        "-02 🚶-Chemin rivière"
                    )
                ).set_author(name="Lieu choisi : 🛶Rivière aux Crabes", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_riviere_crabes'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_riviere_crabes'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_riviere_crabes':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🚶-Chemin rivière",
                    description=(
                        "🔚-End:\n"
                        "❤️ +15 | ⭐ +350\n"
                        "Ou\n"
                        "🤢 6h | 💔 -5\n"
                        "Ou\n"
                        "😖 40m | ⭐ +10\n"
                        "▬▬\n\n"
                        "🌞-S'installer au bord de la rivière:\n"
                        "🕒 2h | ⭐ +25\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +25\n"
                        "Ou\n"
                        "😴 3h | ❤️ +5 | ⭐ +220\n"
                        "▬▬\n\n"
                        "🌊-Poursuivre votre chemin en marchant dans l'eau: :white_check_mark:\n"
                        "❤️ +5 | ⭐ +350\n"
                        "Ou\n"
                        "😖 40m | 💔 -10\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🦀-Trouver quelque chose pour vous préparer un repas:\n"
                        "🕒 10m | ❤️ +20 | ⭐ +225\n"
                        "Ou\n"
                        "💔 -35\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏰-Château abandonné\n"
                        "-02 🚶-Chemin rivière"
                    )
                ).set_author(name="Lieu choisi : 🛶Rivière aux Crabes", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_riviere_crabes'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_riviere_crabes'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item19':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏞️ -Village rivière\n"
                        "ou\n"
                        "-02 👨‍🌾 -Suicide\n"
                    )
                ).set_author(name="Lieu choisi : 🏞️Rivière Vacarme", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_riviere_vacarme'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_riviere_vacarme'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_riviere_vacarme':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🏞️ -Village rivière",
                    description=(
                        "🔚-End:\n"
                        "🕒 2h45m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🏊-Traverser la rivière en nageant: :white_check_mark: (Risqué)\n"
                        "🥶 1h | 💔 -30\n"
                        "Ou\n"
                        "❤️ +5 | ⭐ +350\n"
                        "▬▬\n\n"
                        "🚣-Tenter de bricoler un petit bateau:\n"
                        "🕒 30m | 💔 -5\n"
                        "Ou\n"
                        "🥶 1h | 💔 -30\n"
                        "Ou\n"
                        "🕒 2h20m | ⭐ +325 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🌉-Chercher un pont plus loin:\n"
                        "🕒 30m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +25m\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +30\n"
                        "Ou\n"
                        "😖 40m | 💔 -25\n"
                        "▬▬\n\n"
                        "🚶-Partir dans une autre direction: :white_check_mark:\n"
                        "🕒 55m | ⭐ +25\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏞️ -Village rivière\n"
                        "-02 👨‍🌾 -Suicide"
                    )
                ).set_author(name="Lieu choisi : 🛶Rivière aux Crabes", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_riviere_vacarme'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_riviere_vacarme'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_riviere_vacarme':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="👨‍🌾 -Suicide",
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ +450 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🦸-Se jeter à sa rescousse:\n"
                        "🕒 1h | 💔 -10\n"
                        "Ou\n"
                        "🕒 3h | ❤️ +15 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "💔 -50\n"
                        "▬▬\n\n"
                        "😐-Le regarder jeter la pierre:\n"
                        "🕒 10m | ⭐ +125 | 💰 +300\n"
                        "Ou\n"
                        "🕒 6h | ⭐ +25 | 💸 -200\n"
                        "▬▬\n\n"
                        "😈-\"L'aider\" en le poussant:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -50\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +300\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏞️ -Village rivière\n"
                        "-02 👨‍🌾 -Suicide"
                    )
                ).set_author(name="Lieu choisi : 🛶Rivière aux Crabes", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_riviere_vacarme'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_riviere_vacarme'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item20':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🔒-Coffret\n"
                        "ou\n"
                        "-02 🌠-Etoile filante\n"
                        "ou\n"
                        "-03 🐯-Fauves"
                    )
                ).set_author(name="Lieu choisi : 🛣️Route des Merveilles", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_route_merveilles':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🔒-Coffret",
                    description=(
                        "🔚-End:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🔑-Chercher la clef autour du lieu de découverte:\n"
                        "🕒 50m | ⭐ +125 | 💰 +576\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +125 | 💰 +139\n"
                        "Ou\n"
                        "🕒 40m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 2h | ⭐ +25\n"
                        "▬▬\n\n"
                        "⛏️-Attaquer le cadenas à coups de pioche:\n"
                        "🕒 30m | ⭐ +25 (×2)\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +125 | 💰 +68\n"
                        "▬▬\n\n"
                        "▶️ -Abandonner le coffret à l'endroit où vous l'avez trouvé: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🔒-Coffret\n"
                        "-02 🌠-Etoile filante\n"
                        "-03 🐯-Fauves"
                    )
                ).set_author(name="Lieu choisi : 🛶Rivière aux Crabes", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_route_merveilles':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🌠-Étoile filante",
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🗣️-Faire un vœu:\n"
                        "🕒 10m | ⭐ +125 | 💰 +1040\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +25 (×3)\n"
                        "Ou\n"
                        "🕒 10m | 💔 -5\n"
                        "▬▬\n\n"
                        "🏃-Ignorer cet évènement:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "💔 -20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🔒-Coffret\n"
                        "-02 🌠-Étoile filante\n"
                        "-03 🐯-Fauves"
                    )
                ).set_author(name="Lieu choisi : 🛶Rivière aux Crabes", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '03_route_merveilles':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🐯-Fauves",
                    description=(
                        "🔚-End:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💰 +195 | ⭐ +250\n"
                        "Ou\n"
                        "😖 40m | ⭐ +10\n"
                        "▬▬\n\n"
                        "👀-Assister au spectacle:\n"
                        "🕛 25m | ⭐ +25 | 💸 -70\n"
                        "Ou\n"
                        "⭐ +150 (×2)\n"
                        "▬▬\n\n"
                        "🗯️-Crier à la honte:\n"
                        "🕛 30m | ⭐ +25 (×2)\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +195\n"
                        "Ou\n"
                        "😵‍💫 12h | 💔 -25\n"
                        "▬▬\n\n"
                        "🚶‍♂️-Partir:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "🧐 4h30m\n"
                        "Ou\n"
                        "💔 -5 | 💰 +87 | 🔨 Item\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🔒-Coffret\n"
                        "-02 🌠-Étoile filante\n"
                        "-03 🐯-Fauves"
                    )
                ).set_author(name="Lieu choisi : 🛶Rivière aux Crabes", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_route_merveilles'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page4'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item21':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="Voici l'issues possibles :",
                    description=(
                        "-01 🚶-Pluie"
                    )
                ).set_author(name="Lieu choisi : 🛣️Route Grimpante", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_grimpante'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_route_grimpante':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🚶Pluie",
                    description=(
                        "🔚-End:\n"
                        "🕒 15m | ❤️ +5 | ⭐ +225\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🚶-Continuer à marcher:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🏃-Accélérer afin de ne pas trop se mouiller:\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🚶-Pluie"
                    )
                ).set_author(name="Lieu choisi : 🛣️Route Grimpante", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_grimpante'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item22':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="Voici l'issues possibles :",
                    description=(
                        "-01 👼 -Culte\n"
                        "ou\n"
                        "-02 🧪-L'alchimiste"
                    )
                ).set_author(name="Lieu choisi : 🛣️Route Marécageuse", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_marécageuse'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_route_marécageuse'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_route_marécageuse':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="👼 -Culte",
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "✅-Accepter de la rejoindre:\n"
                        "🕒 3h | ⭐ +25\n"
                        "Ou\n"
                        "🕒 30m | ⭐ +25\n"
                        "Ou\n"
                        "🕒 15m | 💔 -25\n"
                        "Ou\n"
                        "🕒 20m | ⭐ +325 | 🔨 Item\n"
                        "▬▬\n\n"
                        "❌-Refuser gentiment la proposition:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 2h | 💔 -10\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 👼 -Culte\n"
                        "-02 🧪-L'alchimiste"
                    )
                ).set_author(name="Lieu choisi : 🛣️Route Grimpante", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_marécageuse'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_route_marécageuse'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_route_marécageuse':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🧪-L'alchimiste",
                    description=(
                        "🔚-End:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20\n"
                        "▬▬\n\n"
                        "🍵-Aller chez l'alchimiste: :white_check_mark:\n"
                        "❤️ +25 | ⭐ +325 | 💸 -300\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "❤️ +25 | ⭐ +350\n"
                        "Ou\n"
                        "😖 40m | ⭐ +10\n"
                        "▬▬\n\n"
                        "🏃-Prendre le raccourci:\n"
                        "😵 12h | 💔 -50\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +15\n"
                        "Ou\n"
                        "⭐ +150 | 💰 +85\n"
                        "▬▬\n\n"
                        "🚶-Continuer le trajet:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 👼 -Culte\n"
                        "-02 🧪-L'alchimiste"
                    )
                ).set_author(name="Lieu choisi : 🛣️Route Grimpante", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_route_marécageuse'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_route_marécageuse'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item23':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="Voici l'issues possibles :",
                    description=(
                        "-01 🏯-Artéfact\n"
                        "ou\n"
                        "-02 🏜️ -Oasis"
                    )
                ).set_author(name="Lieu choisi : 🏜️Vallée des Rois", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_vallee_roi'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_vallee_roi'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_vallee_roi':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🏯-Artéfact",
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "💔 -5 | 💸 -700\n"
                        "Ou\n"
                        "❤️ +30 | ⭐ +350\n"
                        "Ou\n"
                        "🤕 6h | 💔 -10\n"
                        "▬▬\n\n"
                        "⚔️-Combattre le chevalier: :white_check_mark: (Risqué)\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +125 | 💰 +500\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item (×2)\n"
                        "Ou\n"
                        "🤕 6h | 💔 -35\n"
                        "Ou\n"
                        "😵 12h | 💔 -120\n"
                        "▬▬\n\n"
                        "🤝-Faire connaissance avec lui:\n"
                        "⭐ +150 (×4)\n"
                        "Ou\n"
                        "😵 12h | 💔 -75\n"
                        "Ou\n"
                        "🤕 6h | 💔 -30\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +500\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏯-Artéfact\n"
                        "-02 🏜️-Oasis"
                    )
                ).set_author(name="Lieu choisi : 🏜️Vallée des Rois", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_vallee_roi'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_vallee_roi'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_vallee_roi':
                embed = discord.Embed(
                    color=0x00ff00,
                    title="🏜️-Oasis",
                    description=(
                        "🔚-End:\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🍖- Accepter de se joindre à lui:\n"
                        "🤢 6h | 💔 -30\n"
                        "Ou\n"
                        "❤️ +40 | ⭐ +350 (×2)\n"
                        "▬▬\n\n"
                        "💸-Accepter et profiter de la nuit pour lui dérober ses biens:\n"
                        "💰 +525 | ⭐ +550 | 🔨 Item\n"
                        "Ou\n"
                        "🤕 6h | 💔 -60\n"
                        "Ou\n"
                        "🕛 40m | 💸 -250 | ⭐ +25\n"
                        "Ou\n"
                        "💔 -15\n"
                        "▬▬\n\n"
                        "❌-Refuser son offre et poursuivre votre route:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "🕛 10m | ⭐ +25\n"
                        "Ou\n"
                        "🔨 Item | ⭐ +450\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏯-Artéfact\n"
                        "-02 🏜️-Oasis"
                    )
                ).set_author(name="Lieu choisi : 🏜️Vallée des Rois", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_vallee_roi'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_vallee_roi'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item24':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🚶-Puit\n"
                        "ou\n"
                        "-02  🤩-Cadeau\n"
                        "ou\n"
                        "-03 🏝️ -Cocotier\n"
                        "ou\n"
                        "-04 🏚️-Sanctuaire"
                    )
                ).set_author(name="Lieu choisi : 🛖Village Coco", icon_url="https://example.com/your-icon.png")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_village_coco'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_village_coco':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🚶-Puit',
                    description=(
                        "🔚-End:\n"
                        "🕒 25m | ⭐ +25\n"
                        "Ou\n"
                        "🤕 6h | 💔 -45\n"
                        "▬▬\n\n"
                        "👇-Tenter de descendre pour récupérer l'objet: :white_check_mark:\n"
                        "🕒 2h30m | 💔 -30\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +150\n"
                        "▬▬\n\n"
                        "🤝-Tenter d'attraper l'objet avec le seau du puits:\n"
                        "🕒 1h | ⭐ +25\n"
                        "Ou\n"
                        "😖 40m | 💔 -40\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +150\n"
                        "▬▬\n\n"
                        "🚶-Continuer votre route:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 1h | ⭐ +25 | 💸 -75\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🚶-Puit\n"
                        "-02 🤩-Cadeau\n"
                        "-03 🏝️-Cocotier\n"
                        "-04 🏚️-Sanctuaire"
                    )
                ).set_author(name="Lieu choisi : 🛖Village Coco")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_village_coco'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_village_coco':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🤩-Cadeau',
                    description=(
                        "🔚-End: :white_check_mark:\n"
                        "⭐ +550 | 💰 +250 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +450\n"
                        "▬▬\n\n"
                        "🍀-Cadeau en nature:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "😖 40m | 💔 -10\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "▬▬\n\n"
                        "💰-Cadeau en monnaie:\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 1h35m | ⭐ +125 | 💰 +350\n"
                        "Ou\n"
                        "🕒 3h10m | ⭐ +25\n"
                        "▬▬\n\n"
                        "😇-Cadeau en santé:\n"
                        "❤️ +30 | ⭐ +350\n"
                        "Ou\n"
                        "💔 -20\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🥗-Cadeau alimentaire:\n"
                        "🤢 6h | 💸 -300\n"
                        "Ou\n"
                        "❤️ +20 | ⭐ +650 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🚶-Puit\n"
                        "-02 🤩-Cadeau\n"
                        "-03 🏝️-Cocotier\n"
                        "-04 🏚️-Sanctuaire"
                    )
                ).set_author(name="Lieu choisi : 🛖Village Coco")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_village_coco'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '03_village_coco':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏝️-Cocotier',
                    description=(
                        "🔚-End:\n"
                        "🕒 10m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "😴-Continuer votre sieste au pied de l'arbre:\n"
                        "🤕 6h | 💔 -30\n"
                        "Ou\n"
                        "🕒 1h | ❤️ +10 | ⭐ +225\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20 | 💸 -50\n"
                        "▬▬\n\n"
                        "🗣️-Aborder les villageois pour les questionner:\n"
                        "❤️ +15 | ⭐ +350 | 💸 -50\n"
                        "Ou\n"
                        "💔 -15 | 💸 -100\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "🚶-Quitter le village sans plus attendre: :white_check_mark:\n"
                        "❤️ +10 | ⭐ +350\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -100\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🚶-Puit\n"
                        "-02 🤩-Cadeau\n"
                        "-03 🏝️-Cocotier\n"
                        "-04 🏚️-Sanctuaire"
                    )
                ).set_author(name="Lieu choisi : 🛖Village Coco")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_village_coco'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '04_village_coco':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏚️-Sanctuaire',
                    description=(
                        "🔚-End:\n"
                        "😖 40m | 💔 -25\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🚶-Aller au sanctuaire en solitaire:\n"
                        "🤕 6h | 💔 -40\n"
                        "Ou\n"
                        "🤢 6h | 💔 -10\n"
                        "Ou\n"
                        "🕒 1h15m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 1h30m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "⤴️-Demander au groupe de les rejoindre:\n"
                        "🕒 3h30m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "💔 -20\n"
                        "▬▬\n\n"
                        "🔊-Discuter avec le groupe: :white_check_mark:\n"
                        "🕒 30m | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬\n\n"
                        "▶️-Continuer votre route:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +25 | 💸 -300\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🚶-Puit\n"
                        "-02 🤩-Cadeau\n"
                        "-03 🏝️ -Cocotier\n"
                        "-04 🏚️-Sanctuaire"
                    )
                ).set_author(name="Lieu choisi : 🛖Village Coco")
                
                view = View()
                # Ajouter les boutons de la première ligne
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_village_coco'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='04', custom_id='04_village_coco'))
                
                # Ajouter les boutons de la seconde ligne
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item25':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🏠-Maison Abandonnée\n"
                        "ou\n"
                        "-02 🚶-Pendaison\n"
                        "ou\n"
                        "-03 ⚔-Seigneur"
                    )
                ).set_author(name="Lieu choisi : 🏘️Ville Forte", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_ville_forte':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🏠-Maison Abandonnée',
                    description=(
                        "🔚-End:\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🚪-Aller visiter l'intérieur:\n"
                        "🤕 6h | 💔 -25\n"
                        "Ou\n"
                        "🕒 55m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "😴 3h | ⭐ +20\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "🚶-Ne pas s'arrêter et continuer sa route: :white_check_mark:\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏠-Maison Abandonnée\n"
                        "-02 🚶-Pendaison\n"
                        "-03 ⚔-Seigneur"
                    )
                ).set_author(name="Lieu choisi : 🏘️Ville Forte", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_ville_forte':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🚶-Pendaison',
                    description=(
                        "🔚-End:\n"
                        "🕒 15m | ⭐ +25\n"
                        "▬▬\n\n"
                        "💸-Voler des passants assistant au massacre:\n"
                        "🕒 30m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 25m | 💔 -15\n"
                        "▬▬\n\n"
                        "👊-S'interposer et empêcher cet homme de mourir:\n"
                        "🕒 15m | ⭐ +325 | 🔨 Item\n"
                        "Ou\n"
                        "🕒 15m | 💔 -10\n"
                        "Ou\n"
                        "🕒 20m | 💔 -15 | 💸 -200\n"
                        "Ou\n"
                        "🪦 Mort\n"
                        "▬▬\n\n"
                        "🚶-Continuer votre route paisiblement: :white_check_mark:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🕒 10m | ⭐ +125 | 💰 +75\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏠-Maison Abandonnée\n"
                        "-02 🚶-Pendaison\n"
                        "-03 ⚔-Seigneur"
                    )
                ).set_author(name="Lieu choisi : 🏘️Ville Forte", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '03_ville_forte':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='⚔-Seigneur',
                    description=(
                        "🔚-End:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "🔒 24h\n"
                        "▬▬\n\n"
                        "⚔-Aider les villageois à se débarrasser du seigneur:\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "🤕 6h | 💸 -160\n"
                        "Ou\n"
                        "💔 -15\n"
                        "Ou\n"
                        "😵 12h | 💔 -120\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +1200\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +800\n"
                        "Ou\n"
                        "⭐ +550 | 💰 +100 | 🔨 Item\n"
                        "▬▬\n\n"
                        "🗣️-Répéter au seigneur ce que vous avez entendu:\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +25\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +100\n"
                        "Ou\n"
                        "🤕 6h | 💔 -60\n"
                        "▬▬\n\n"
                        "🚶-Ne pas prendre de risques et s'en aller au plus vite: :white_check_mark:\n"
                        "💔 -5 | 💸 -300\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "Ou\n"
                        "❤️ +10 | ⭐ +350\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150 | 💸 -250\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🏠-Maison Abandonnée\n"
                        "-02 🚶-Pendaison\n"
                        "-03 ⚔-Seigneur"
                    )
                ).set_author(name="Lieu choisi : 🏘️Ville Forte", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='03', custom_id='03_ville_forte'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page5'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item26':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 ⛲-Fontaine\n"
                        "ou\n"
                        "-02 🥳 -Festin"
                    )
                ).set_author(name="Lieu choisi : 🛣️Voie champêtre", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_voie_champetre'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_voie_champetre'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page6'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_voie_champetre':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='⛲-Fontaine',
                    description=(
                        "🔚-End:\n"
                        "🕒 1h | ⭐ +125 | 💰 +65\n"
                        "▬▬\n\n"
                        "💦-Se reposer et boire pour reprendre des forces: :white_check_mark:\n"
                        "🕒 30m | ❤️ +5 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 1h | ❤️ +15 | ⭐ +225\n"
                        "Ou\n"
                        "🕒 3h\n"
                        "▬▬\n\n"
                        "🚶-Ne pas s'arrêter et continuer sa route:\n"
                        "⭐ +150 (×4)\n"
                        "Ou\n"
                        "😴 3h | 💔 -30\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 ⛲-Fontaine\n"
                        "-02 🥳-Festin"
                    )
                ).set_author(name="Lieu choisi : 🛣️Voie champêtre", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_voie_champetre'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_voie_champetre'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page6'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '02_voie_champetre':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🥳-Festin',
                    description=(
                        "🔚-End:\n"
                        "😖 40m | 💔 -20\n"
                        "Ou\n"
                        "🕒 3h | ❤️ +40 | ⭐ +225\n"
                        "▬▬\n\n"
                        "👄-S'asseoir tranquillement pour bavarder: :white_check_mark:\n"
                        "🕒 2h | ⭐ +25\n"
                        "Ou\n"
                        "⭐ +450 | 🔨 Item\n"
                        "Ou\n"
                        "⭐ +150 (×2)\n"
                        "Ou\n"
                        "❤️ +20 | ⭐ +450 | 💰 +400\n"
                        "▬▬\n\n"
                        "🍗-En profiter pour s'empiffrer de nourriture:\n"
                        "❤️ +10 | ⭐ +350\n"
                        "Ou\n"
                        "🤢 6h\n"
                        "Ou\n"
                        "🕒 1h15m | ⭐ +25\n"
                        "Ou\n"
                        "🤪 4h\n"
                        "▬▬\n\n"
                        "🕵️-Profiter de l'animation générale pour voler les gens:\n"
                        "⭐ +250 | 💰 +700\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +250\n"
                        "Ou\n"
                        "🤕 6h | 💔 -20\n"
                        "▬▬\n\n"
                        "🚶-Continuer sans s'arrêter:\n"
                        "⭐ +150 | 💸 -200\n"
                        "Ou\n"
                        "⭐ +250 | 💰 +100\n"
                        "Ou\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 ⛲-Fontaine\n"
                        "-02 🥳-Festin"
                    )
                ).set_author(name="Lieu choisi : 🛣️Voie champêtre", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_voie_champetre'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='02', custom_id='02_voie_champetre'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page6'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'item27':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici les issues possibles :',
                    description=(
                        "-01 🚢-Capitaine"
                    )
                ).set_author(name="Lieu choisi : 🚢Retour Bateau", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_retour_bateau'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page6'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == '01_retour_bateau':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='🚢-Capitaine',
                    description=(
                        "⚠️ Pas de rapport sur le bateau du retour, au risque de se retrouver avec une altération qu'il ne sera pas possible de soigner ⚠️\n\n"
                        "🔚 -End\n"
                        "⚡ +150 | ⭐ +150\n"
                        "▬▬\n\n"
                        "🍺 -Accepter la boisson :white_check_mark:\n"
                        "❤️ +10 | ⭐ +350\n"
                        "OU\n"
                        "❤️ +15 | ⭐ +350\n"
                        "▬▬\n\n"
                        "✋ -Refuser poliment le cadeau\n"
                        "⚡ +150 | ⭐ +150\n"
                        "OU\n"
                        "⚡ +250 | ⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n\n"
                        "Autres choix :\n"
                        "-01 🚢-Capitaine"
                    )
                ).set_author(name="Lieu choisi : 🛣️Voie champêtre", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='01', custom_id='01_retour_bateau'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='page6'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
                await interaction.response.edit_message(embed=embed, view=view)
    
    def create_pagination_view(self, with_close_button=False):
        view = View()
        view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 1', custom_id='page1'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 2', custom_id='page2'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 3', custom_id='page3'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 4', custom_id='page4'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 5', custom_id='page5'))
        
        if with_close_button:
            view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 6', custom_id='page6'))
            view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
        
        return view

    def create_page_buttons(self, page, with_close_button=False):
        if page == '6':
            buttons = [Button(style=discord.ButtonStyle.secondary, label=f'{i:02}', custom_id=f'item{i:02}') for i in range(26, 28)]
            view = View()
            for button in buttons[:5]:
                view.add_item(button)
            view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour au sommaire', custom_id='back'))
        else:
            buttons = [Button(style=discord.ButtonStyle.secondary, label=f'{i:02}', custom_id=f'item{i:02}') for i in range((int(page) - 1) * 5 + 1, int(page) * 5 + 1)]
            view = View()
            for button in buttons:
                view.add_item(button)
            view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour au sommaire', custom_id='back'))
        
        if with_close_button:
            view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='close'))
        
        return view

    def create_page_embed(self, page):
        pages = {
            '1': '🌸-01-Le Berceau\n🌳-02-Bois Hurlant\n🛖-03-Boug-Coton\n🛣️-04-Chemin aux Loups\n🛣️-05-Chemin du Dédale',
            '2': '🏘️-06-Claire De Ville\n🛣️-07-Croisement des Destins\n🏖️-08-La Dune\n🌸-09-L\'Étendue\n🌳-10-Forêt Célestrum',
            '3': '🌳-11-Forêt Du Vieillard\n🛣️-12-Grand Axe\n🛣️-13-Grande Rue\n🛶-14-Lac Mirage\n🏘️-15-Mergagnan',
            '4': '⛰️-16-Mont Célestrum\n🏖️-17-Plage Sentinelle\n🛶-18-Rivière aux Crabes\n🏞️-19-Rivière Vacarme\n🛣️-20-Route des Merveilles',
            '5': '🛣️-21-Route Grimpante\n🛣️-22-Route Marécageuse\n🏜️-23-Vallée des Rois\n🛖-24-Village Coco\n🏘️-25-Ville Forte',
            '6': '🛣️-26-Voie champêtre\n🚢-27-Retour Bateau'
        }
        return discord.Embed(
            color=0x00ff00,
            title=f'Page {page}',
            description=pages.get(page, 'Page non trouvée')
        )

async def setup(bot):
    await bot.add_cog(Issues(bot))
