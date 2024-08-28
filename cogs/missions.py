import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

class Missions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='m', description='Affiche les récompenses des différentes missions')
    async def missions(self, interaction: discord.Interaction):
        user = interaction.user
            # Vérification des rôles
        if not any(role.name in ['Administrateur', 'Modérateur', 'DB player', 'SURVEILLANT SPATIAL', 'LdG', 'Admin'] for role in user.roles):
            await interaction.response.send_message(
                f"{user.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.", ephemeral=True)
            return
        embed = discord.Embed(
            color=0x00ff00,
            title='Voici le sommaire :',
            description=(
                "Page 1 :\n💸-01-dépense\n💰-02-récolter-argent\n⭐-03-gagner-xp\n🔨-04-trouver-objet\n🏅-05-gagner-points\n▬▬\n"
                "Page 2 :\n⚔-06-combats-et-attaques\n🏞️-07-lieux (Aller à ...)\n🏞️-08-lieux (Explorer lieux)\n🚶🏻-09-trajets\n🧪-10-potions\n▬▬\n"
                "Page 3 :\n🌋-11-pve\n🔍-12-rapports\n🤝-13-rencontres\n♥️-14-vie"
            )
        )
        
        view = self.create_pagination_view(with_close_button=True)
        await interaction.response.send_message(embed=embed, view=view)

    # Gestion des interactions
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.component:
            custom_id = interaction.data['custom_id']

            if custom_id == 'missions_close':
                # Suppression du message lorsque le bouton Fermer est cliqué
                await interaction.response.defer()
                await interaction.message.delete()

            elif custom_id == 'missions_back':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Voici le sommaire :',
                    description=(
                        "Page 1 :\n💸-01-dépense\n💰-02-récolter-argent\n⭐-03-gagner-xp\n🔨-04-trouver-objet\n🏅-05-gagner-points\n▬▬\n"
                        "Page 2 :\n⚔-06-combats-et-attaques\n🏞️-07-lieux (Aller à ...)\n🏞️-08-lieux (Explorer lieux)\n🚶🏻-09-trajets\n🧪-10-potions\n▬▬\n"
                        "Page 3 :\n🌋-11-pve\n🔍-12-rapports\n🤝-13-rencontres\n♥️-14-vie"
                    )
                )
                view = self.create_pagination_view(with_close_button=True)
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id.startswith('missions_page'):
                page = custom_id.replace('missions_page', '')
                embed = self.create_page_embed(page)
                view = self.create_page_buttons(page, with_close_button=True)
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item01':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 💸Dépense", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_depense'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_depense'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_depense':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "💸▮-Dépenser 250 d'argent:\n"
                        "\n"
                        "🏅 +53\n"
                        "💰 +13\n"
                        "⭐ +20\n"
                        "💎 +1\n"
                        "▬▬\n"
                        "💸▮-Dépenser 750 d'argent:\n"
                        "\n"
                        "🏅 +245\n"
                        "💰 +38\n"
                        "⭐ +50\n"
                        "💎 +1\n"
                        "▬▬\n"
                        "💸▮-Dépenser 1500 d'argent:\n"
                        "\n"
                        "🏅 +525\n"
                        "💰 +75\n"
                        "⭐ +80\n"
                        "💎 +3\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 💸Dépense", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_depense'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_depense'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_depense':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "💸▮-Dépenser 250 d'argent:\n"
                        "\n"
                        "🕛 1h\n"
                        "🏅 +15\n"
                        "💰 +25\n"
                        "⭐ +20\n"
                        "▬▬\n"
                        "💸▮-Dépenser 500 d'argent:\n"
                        "\n"
                        "🕛 4h\n"
                        "🏅 +50\n"
                        "💰 +50\n"
                        "⭐ +50\n"
                        "▬▬\n"
                        "💸▮-Dépenser 750 d'argent:\n"
                        "\n"
                        "🕛 1j\n"
                        "🏅 +70\n"
                        "💰 +75\n"
                        "⭐ +50\n"
                        "▬▬\n"
                        "💸▮-Dépenser 1500 d'argent:\n"
                        "\n"
                        "🕛 1j\n"
                        "🏅 +150\n"
                        "💰 +150\n"
                        "⭐ +80\n"
                        "▬▬\n"
                        "💸▮-Dépenser 5000 d'argent:\n"
                        "\n"
                        "🕛 1j\n"
                        "🏅 +300\n"
                        "💰 +250\n"
                        "⭐ +120\n"
                        "▬▬\n"
                        "💸▮-Dépenser 7500 d'argent:\n"
                        "\n"
                        "🕛 1j\n"
                        "🏅 +500\n"
                        "💰 +250\n"
                        "⭐ +200\n"
                        "▬▬\n"
                        "💸▮-Dépenser 15000 d'argent:\n"
                        "\n"
                        "🕛 3j\n"
                        "🏅 +1500\n"
                        "💰 +1500\n"
                        "⭐ +400\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 💸Dépense", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_depense'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_depense'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item02':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 💰Récolter Argent", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_recolter_argent'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_recolter_argent'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_recolter_argent':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "💰▮-Récolter 250 pièces:\n"
                        "🏅 +105\n"
                        "⭐ +20\n"
                        "💎 +2\n"
                        "▬▬\n"
                        "💰▮-Récolter 500 pièces:\n"
                        "🏅 +263\n"
                        "⭐ +65\n"
                        "💎 +6\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 💰Récolter Argent", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_recolter_argent'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_recolter_argent'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_recolter_argent':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "💰▮-Récolter 250 pièces:\n"
                        "🕛 1j 12h\n"
                        "🏅 +30\n"
                        "⭐ +20\n"
                        "▬▬\n"
                        "💰▮- Récolter 350 pièces:\n"
                        "🕛 1j 16h\n"
                        "🏅 +45\n"
                        "⭐ +35\n"
                        "▬▬\n"
                        "💰▮- Récolter 500 pièces:\n"
                        "🕛 2j 8h\n"
                        "🏅 +75\n"
                        "⭐ +65\n"
                        "▬▬\n"
                        "💰▮- Récolter 1000 pièces:\n"
                        "🕛 3j\n"
                        "🏅 +100\n"
                        "⭐ +140\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 💰Récolter Argent", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_recolter_argent'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_recolter_argent'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item03':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : ⭐Gagner xp", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_gagner_xp'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_gagner_xp'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_gagner_xp':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "⭐▮-Gagner 300 expériences:\n"
                        "🏅 +53\n"
                        "💰 +8\n"
                        "💎 +2\n"
                        "▬▬\n"
                        "⭐▮-Gagner 400 expériences:\n"
                        "🏅 +70\n"
                        "💰 +13\n"
                        "💎 +3\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : ⭐Gagner xp", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_gagner_xp'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_gagner_xp'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_gagner_xp':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "⭐▮-Gagner 300 expériences:\n"
                        "🕛 1j 12h\n"
                        "🏅 +15\n"
                        "💰 +20\n"
                        "▬▬\n"
                        "⭐▮-Gagner 400 expériences:\n"
                        "🕛 1j 12h\n"
                        "🏅 +15\n"
                        "💰 +25\n"
                        "▬▬\n"
                        "⭐▮-Gagner 1000 expériences:\n"
                        "🕛 3j\n"
                        "🏅 +35\n"
                        "💰 +50\n"
                        "▬▬\n"
                        "⭐▮-Gagner 2000 expériences:\n"
                        "🕛 4j\n"
                        "🏅 +50\n"
                        "💰 +100\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : ⭐Gagner xp", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_gagner_xp'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_gagner_xp'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item04':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🔨Trouver Objet", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_trouver_objet'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_trouver_objet'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_trouver_objet':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "🔨▮-Trouver ou acheter 1 objet:\n"
                        "🏅 +70\n"
                        "💰 +25\n"
                        "⭐ +30\n"
                        "💎 +2\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🔨Trouver Objet", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_trouver_objet'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_trouver_objet'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_trouver_objet':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "🔨▮-Trouver ou acheter 1 objet:\n"
                        "🕛 1j\n"
                        "🏅 +20\n"
                        "💰 +50\n"
                        "⭐ +30\n"
                        "▬▬\n"
                        "🔨▮-Trouver ou acheter 5 objets:\n"
                        "🕛 3j\n"
                        "🏅 +60\n"
                        "💰 +125\n"
                        "⭐ +60\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🔨Trouver Objet", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_trouver_objet'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_trouver_objet'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item05':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏅Gagner Points", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_gagner_points'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_gagner_points'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_gagner_points':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "🏅▮-Gagner 500 points:\n"
                        "💰 +13\n"
                        "⭐ +10\n"
                        "💎 +1\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏅Gagner Points", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_gagner_points'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_gagner_points'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_gagner_points':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "🏅▮-Gagner 500 points:\n"
                        "🕛 1j\n"
                        "💰 +25\n"
                        "⭐ +10\n"
                        "▬▬\n"
                        "🏅▮-Gagner 1500 points:\n"
                        "🕛 2j\n"
                        "💰 +75\n"
                        "⭐ +40\n"
                        "▬▬\n"
                        "🏅▮-Gagner 3000 points:\n"
                        "🕛 3j\n"
                        "💰 +125\n"
                        "⭐ +100\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏅Gagner Points", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_gagner_points'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_gagner_points'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page1'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item06':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires (Combats)\n"
                        "ou\n"
                        "📙-Secondaires (Attaques Précises)"
                    )
                ).set_author(name="Thème choisi : ⚔Combats et Attaques", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Combats)', custom_id='missions_02_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Attaques Précises)', custom_id='missions_03_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_combats_attaques':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "⚔️▮-Faire 1 combat:\n"
                        "🏅 +88\n"
                        "💰 +13\n"
                        "⭐ +20\n"
                        "💎 +1\n"
                        "▬▬\n"
                        "⚔️▮-Faire 3 combats:\n"
                        "🏅 +175\n"
                        "💰 +25\n"
                        "⭐ +40\n"
                        "💎 +2\n"
                        "▬▬\n"
                        "⚔️▮-Faire 5 combats:\n"
                        "🏅 +263\n"
                        "💰 +38\n"
                        "⭐ +60\n"
                        "💎 +3\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires (Combats)\n"
                        "📙-Secondaires (Attaques Précises)"
                    )
                ).set_author(name="Thème choisi : ⚔Combats et Attaques", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Combats)', custom_id='missions_02_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Attaques Précises)', custom_id='missions_03_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_combats_attaques':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires (Combats)',
                    description=(
                        "⚔️▮-Faire 1 combat:\n"
                        "🕛 1j\n"
                        "🏅 +25\n"
                        "💰 +25\n"
                        "⭐ +20\n"
                        "▬▬\n"
                        "⚔️▮-Faire 3 combats:\n"
                        "🕛 18h\n"
                        "🏅 +50\n"
                        "💰 +50\n"
                        "⭐ +40\n"
                        "▬▬\n"
                        "⚔️▮-Faire 5 combats:\n"
                        "🕛 12h\n"
                        "🏅 +75\n"
                        "💰 +75\n"
                        "⭐ +60\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires (Combats)\n"
                        "📙-Secondaires (Attaques Précises)"
                    )
                ).set_author(name="Thème choisi : ⚔Combats et Attaques", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Combats)', custom_id='missions_02_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Attaques Précises)', custom_id='missions_03_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_03_combats_attaques':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires (Attaques Précises)',
                    description=(
                        "🪓▮-Faire 1 attaque précise:\n"
                        "🕛 1j\n"
                        "🏅 +15\n"
                        "💰 +25\n"
                        "⭐ +20\n"
                        "▬▬\n"
                        "🪓▮-Faire 5 attaques précises:\n"
                        "🕛 1j\n"
                        "🏅 +25\n"
                        "💰 +50\n"
                        "⭐ +40\n"
                        "▬▬\n"
                        "🪓▮-Faire 10 attaques précises:\n"
                        "🕛 1j\n"
                        "🏅 +50\n"
                        "💰 +100\n"
                        "⭐ +60\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires (Combats)\n"
                        "📙-Secondaires (Attaques Précises)"
                    )
                ).set_author(name="Thème choisi : ⚔Combats et Attaques", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Combats)', custom_id='missions_02_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Attaques Précises)', custom_id='missions_03_combats_attaques'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item07':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏞️Lieux (Aller à ...)", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_lieux_01'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_lieux_01'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_lieux_01':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "🏡▮-Aller à ... :\n"
                        "🏅 +963\n"
                        "💰 +75\n"
                        "⭐ +135\n"
                        "💎 +7\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏞️Lieux (Aller à ...)", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_lieux_01'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_lieux_01'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_lieux_01':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "🏡▮-Aller à ... :\n"
                        "🕛 7j\n"
                        "🏅 +250\n"
                        "💰 +145\n"
                        "⭐ +125\n"
                        "▬▬\n"
                        "🏡▮-Aller à ... :\n"
                        "🕛 3j\n"
                        "🏅 +275\n"
                        "💰 +150\n"
                        "⭐ +135\n"
                        "▬▬\n"
                        "🏡▮-Aller à ... :\n"
                        "🕛 2j\n"
                        "🏅 +300\n"
                        "💰 +175\n"
                        "⭐ +160\n"
                        "▬▬\n"
                        "🏡▮-Aller à ... :\n"
                        "🕛 1j\n"
                        "🏅 +350\n"
                        "💰 +260\n"
                        "⭐ +240\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏞️Lieux (Aller à ...)", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_lieux_01'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_lieux_01'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item08':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏞️Lieux (Explorer lieux)", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_lieux_02'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_lieux_02'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_lieux_02':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "🏘️▮-Explorer 3 lieux:\n"
                        "🏅 +175\n"
                        "💰 +50\n"
                        "⭐ +75\n"
                        "💎 +3\n"
                        "▬▬\n"
                        "🏘️▮-Explorer 5 lieux:\n"
                        "🏅 +525\n"
                        "💰 +100\n"
                        "⭐ +150\n"
                        "💎 +7\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏞️Lieux (Explorer lieux)", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_lieux_02'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_lieux_02'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_lieux_02':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "🏘️▮-Explorer 3 lieux:\n"
                        "🕛 1j\n"
                        "🏅 +50\n"
                        "💰 +100\n"
                        "⭐ +75\n"
                        "▬▬\n"
                        "🏘️▮-Explorer 5 lieux:\n"
                        "🕛 1j\n"
                        "🏅 +150\n"
                        "💰 +200\n"
                        "⭐ +150\n"
                        "▬▬\n"
                        "🏘️▮-Explorer 10 lieux:\n"
                        "🕛 3j\n"
                        "🏅 +175\n"
                        "💰 +300\n"
                        "⭐ +250\n"
                        "▬▬\n"
                        "🏘️▮-Explorer 15 lieux:\n"
                        "🕛 4j 12h\n"
                        "🏅 +250\n"
                        "💰 +400\n"
                        "⭐ +375\n"
                        "▬▬\n"
                        "🏘️▮-Explorer 20 lieux:\n"
                        "🕛 7j\n"
                        "🏅 +390\n"
                        "💰 +550\n"
                        "⭐ +425\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🏞️Lieux (Explorer lieux)", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_lieux_02'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_lieux_02'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item09':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🚶🏻Trajets", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_trajets'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_trajets'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_trajets':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "⌚▮-Faire 1 trajet d'au moins 3h:\n"
                        "🏅 +105\n"
                        "💰 +33\n"
                        "⭐ +10\n"
                        "💎 +1\n"
                        "▬▬\n"
                        "⌚▮-Faire 1 trajet d'au moins 2h:\n"
                        "🏅 +490\n"
                        "💰 +43\n"
                        "⭐ +30\n"
                        "💎 +4\n"
                        "▬▬\n"
                        "⌚▮-Faire 2 trajets d'au moins 2h:\n"
                        "🏅 +858\n"
                        "💰 +98\n"
                        "⭐ +250\n"
                        "💎 +8\n"
                        "▬▬\n"
                        "⌚▮-Faire 2 trajets d'au moins 3h:\n"
                        "🏅 +158\n"
                        "💰 +83\n"
                        "⭐ +150\n"
                        "💎 +5\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🚶🏻Trajets", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_trajets'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_trajets'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_trajets':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "⌚▮-Faire 1 trajet de 2-3h:\n"
                        "🕛 1j\n"
                        "🏅 +30\n"
                        "💰 +65\n"
                        "⭐ +10\n"
                        "▬▬\n"
                        "⌚▮-Faire 2 trajets de 2-3h:\n"
                        "🕛 2j\n"
                        "🏅 +45\n"
                        "💰 +165\n"
                        "⭐ +150\n"
                        "▬▬\n"
                        "⌚▮-Faire 1 trajet de 5-7h:\n"
                        "🕛 3j\n"
                        "🏅 +140\n"
                        "💰 +85\n"
                        "⭐ +30\n"
                        "▬▬\n"
                        "⌚▮-Faire 2 trajets de 5-7h:\n"
                        "🕛 3j 18h\n"
                        "🏅 +245\n"
                        "💰 +195\n"
                        "⭐ +250\n"
                        "▬▬\n"
                        "⌚▮-Faire 1 trajet de 9h:\n"
                        "🕛 5j\n"
                        "🏅 +185\n"
                        "💰 +125\n"
                        "⭐ +50\n"
                        "▬▬\n"
                        "⌚▮-Faire 2 trajets de 9h:\n"
                        "🕛 6j 6h\n"
                        "🏅 +290\n"
                        "💰 +235\n"
                        "⭐ +350\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🚶🏻Trajets", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_trajets'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_trajets'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item10':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🧪Potions", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_potions'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_potions'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_potions':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "🚱▮-Boire 1 potion sans effet:\n"
                        "🏅 +315\n"
                        "💰 +65\n"
                        "⭐ +75\n"
                        "💎 +2\n"
                        "▬▬\n"
                        "🚱▮-Boire 2 potions sans effet:\n"
                        "🏅 +840\n"
                        "💰 +88\n"
                        "⭐ +140\n"
                        "💎 +5\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🧪Potions", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_potions'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_potions'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_potions':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "🚱▮-Boire 1 potion sans effet:\n"
                        "🕛 1j\n"
                        "🏅 +90\n"
                        "💰 +130\n"
                        "⭐ +75\n"
                        "▬▬\n"
                        "🚱▮-Boire 2 potions sans effet:\n"
                        "🕛 1j\n"
                        "🏅 +240\n"
                        "💰 +170\n"
                        "⭐ +140\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🧪Potions", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_potions'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_potions'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page2'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item11':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📙-Secondaires (Rage)\n"
                        "ou\n"
                        "📙-Secondaires (Boss)"
                    )
                ).set_author(name="Thème choisi : 🌋Pve", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Rage)', custom_id='missions_01_pve'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Boss)', custom_id='missions_02_pve'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_pve':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires (Rage)',
                    description=(
                        "🤬▮-Gagner 1 point de rage:\n"
                        "🕛 3j\n"
                        "🏅 +25\n"
                        "💰 +10\n"
                        "⭐ +85\n"
                        "▬▬\n"
                        "🤬▮-Gagner 3 points de rage:\n"
                        "🕛 7j\n"
                        "🏅 +75\n"
                        "💰 +30\n"
                        "⭐ +285\n"
                        "▬▬\n"
                        "🤬▮-Gagner 5 points de rage:\n"
                        "🕛 10j 12h\n"
                        "🏅 +125\n"
                        "💰 +50\n"
                        "⭐ +385\n"
                        "▬▬\n"
                        "🤬▮-Gagner 10 points de rage:\n"
                        "🕛 10j 12h\n"
                        "🏅 +200\n"
                        "💰 +100\n"
                        "⭐ +885\n"
                        "▬▬\n"
                        "🤬▮-Gagner 15 points de rage:\n"
                        "🕛 7j\n"
                        "🏅 +450\n"
                        "💰 +150\n"
                        "⭐ +1085\n"
                        "▬▬\n"
                        "🤬▮-Gagner 25 points de rage:\n"
                        "🕛 21j\n"
                        "🏅 +250\n"
                        "💰 +250\n"
                        "⭐ +1885\n"
                        "▬▬\n"
                        "🤬▮-Gagner 100 points de rage:\n"
                        "🕛 105j\n"
                        "🏅 +320\n"
                        "💰 +1000\n"
                        "⭐ +8885\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📙-Secondaires (Rage)\n"
                        "📙-Secondaires (Boss)"
                    )
                ).set_author(name="Thème choisi : 🌋Pve", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Rage)', custom_id='missions_01_pve'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Boss)', custom_id='missions_02_pve'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_pve':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires (Boss)',
                    description=(
                        "👹▮-Battre 1 boss:\n"
                       "🕛 4j 4h\n"
                        "🏅 +115\n"
                        "💰 +50\n"
                        "⭐ +100\n"
                        "▬▬\n"
                        "👹▮-Battre 2 boss:\n"
                        "🕛 4j 4h\n"
                        "🏅 +185\n"
                        "💰 +100\n"
                        "⭐ +200\n"
                        "▬▬\n"
                        "👹▮-Battre 3 boss:\n"
                        "🕛 4j 4h\n"
                        "🏅 +275\n"
                        "💰 +150\n"
                        "⭐ +300\n"
                        "▬▬\n"
                        "👹▮-Battre 5 boss:\n"
                        "🕛 8j 8h\n"
                        "🏅 +350\n"
                        "💰 +300\n"
                        "⭐ +500\n"
                        "▬▬\n"
                        "👹▮-Battre 10 boss:\n"
                        "🕛 12j 12h\n"
                        "🏅 +620\n"
                        "💰 +500\n"
                        "⭐ +1000\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📙-Secondaires (Rage)\n"
                        "📙-Secondaires (Boss)"
                    )
                ).set_author(name="Thème choisi : 🌋Pve", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Rage)', custom_id='missions_01_pve'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙(Boss)', custom_id='missions_02_pve'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item12':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🔍Rapports", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_rapports'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_rapports'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_rapports':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "📜▮-Faire 3 rapports:\n"
                        "🏅 +88\n"
                        "💰 +15\n"
                        "⭐ +10\n"
                        "💎 +1\n"
                        "▬▬\n"
                        "📜▮-Faire 5 rapports:\n"
                        "🏅 +175\n"
                        "💰 +25\n"
                        "⭐ +20\n"
                        "💎 +3\n"
                        "▬▬\n"
                        "📜▮-Faire 10 rapports:\n"
                        "🏅 +263\n"
                        "💰 +40\n"
                        "⭐ +50\n"
                        "💎 +5\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🔍Rapports", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_rapports'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_rapports'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_rapports':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "📜▮-Faire 3 rapports:\n"
                        "🕛 12h\n"
                        "🏅 +25\n"
                        "💰 +30\n"
                        "⭐ +10\n"
                        "▬▬\n"
                        "📜▮-Faire 5 rapports:\n"
                        "🕛 1j 16h\n"
                        "🏅 +50\n"
                        "💰 +50\n"
                        "⭐ +20\n"
                        "▬▬\n"
                        "📜▮-Faire 10 rapports:\n"
                        "🕛 2j 2h\n"
                        "🏅 +75\n"
                        "💰 +80\n"
                        "⭐ +50\n"
                        "▬▬\n"
                        "📜▮-Faire 15 rapports:\n"
                        "🕛 2j 12h\n"
                        "🏅 +100\n"
                        "💰 +110\n"
                        "⭐ +70\n"
                        "▬▬\n"
                        "📜▮-Faire 25 rapports:\n"
                        "🕛 3j 13h\n"
                        "🏅 +125\n"
                        "💰 +150\n"
                        "⭐ +120\n"
                        "▬▬\n"
                        "📜▮-Faire 30 rapports:\n"
                        "🕛 4j\n"
                        "🏅 +150\n"
                        "💰 +165\n"
                        "⭐ +150\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🔍Rapports", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_rapports'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_rapports'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item13':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🤝Rencontres", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_rencontres'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_rencontres'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_rencontres':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "👥▮-Rencontrer 2 joueurs:\n"
                        "🏅 +263\n"
                        "💰 +18\n"
                        "⭐ +25\n"
                        "💎 +1\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🤝Rencontres", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_rencontres'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_rencontres'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_rencontres':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "👥▮-Rencontrer 2 joueurs:\n"
                        "🕛 1j\n"
                        "🏅 +75\n"
                        "💰 +35\n"
                        "⭐ +25\n"
                        "▬▬\n"
                        "👥▮-Rencontrer 5 joueurs:\n"
                        "🕛 2j\n"
                        "🏅 +125\n"
                        "💰 +50\n"
                        "⭐ +100\n"
                        "▬▬\n"
                        "👥▮-Rencontrer 8 joueurs:\n"
                        "🕛 3j\n"
                        "🏅 +175\n"
                        "💰 +95\n"
                        "⭐ +175\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : 🤝Rencontres", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_rencontres'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_rencontres'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_item14':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='Choissisez entre :',
                    description=(
                        "📘-Quotidiennes\n"
                        "ou\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : ♥️Vie", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_vie'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_vie'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_01_vie':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📘-Quotidiennes',
                    description=(
                        "💗▮-Gagner 10 pv:\n"
                        "🕛 1j\n"
                        "🏅 +210\n"
                        "💰 +20\n"
                        "⭐ +20\n"
                        "💎 +2\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : ♥️Vie", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_vie'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_vie'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)

            elif custom_id == 'missions_02_vie':
                embed = discord.Embed(
                    color=0x00ff00,
                    title='📙-Secondaires',
                    description=(
                        "💗▮-Gagner 5 pv:\n"
                        "🕛 1j\n"
                        "🏅 +40\n"
                        "💰 +25\n"
                        "⭐ +10\n"
                        "▬▬\n"
                        "💗▮-Gagner 10 pv:\n"
                        "🕛 1j 12h\n"
                        "🏅 +60\n"
                        "💰 +40\n"
                        "⭐ +20\n"
                        "▬▬\n"
                        "💗▮-Gagner 15 pv:\n"
                        "🕛 2j\n"
                        "🏅 +75\n"
                        "💰 +65\n"
                        "⭐ +40\n"
                        "▬▬\n"
                        "💗▮-Gagner 30 pv:\n"
                        "🕛 3j\n"
                        "🏅 +85\n"
                        "💰 +100\n"
                        "⭐ +50\n"
                        "▬▬▬▬▬▬▬▬\n"
                        "Autres choix:\n"
                        "📘-Quotidiennes\n"
                        "📙-Secondaires"
                    )
                ).set_author(name="Thème choisi : ♥️Vie", icon_url="https://example.com/your-icon.png")
                
                view = View()
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📘', custom_id='missions_01_vie'))
                view.add_item(Button(style=discord.ButtonStyle.primary, label='📙', custom_id='missions_02_vie'))
                view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour', custom_id='missions_page3'))
                view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
                await interaction.response.edit_message(embed=embed, view=view)


    def create_pagination_view(self, with_close_button=True):
        view = View()
        view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 1', custom_id='missions_page1'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 2', custom_id='missions_page2'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='Page 3', custom_id='missions_page3'))
        view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
        
        return view

    def create_page_buttons(self, page, with_close_button=False):
        if page == '3':
            buttons = [Button(style=discord.ButtonStyle.secondary, label=f'{i:02}', custom_id=f'missions_item{i:02}') for i in range(11, 15)]
            view = View()
            for button in buttons[:5]:
                view.add_item(button)
            view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour au sommaire', custom_id='missions_back'))
        else:
            buttons = [Button(style=discord.ButtonStyle.secondary, label=f'{i:02}', custom_id=f'missions_item{i:02}') for i in range((int(page) - 1) * 5 + 1, int(page) * 5 + 1)]
            view = View()
            for button in buttons:
                view.add_item(button)
            view.add_item(Button(style=discord.ButtonStyle.secondary, label='Retour au sommaire', custom_id='missions_back'))
        
        if with_close_button:
            view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='missions_close'))
        
        return view

    def create_page_embed(self, page):
        pages = {
            '1': '💸-01-dépense\n💰-02-récolter-argent\n⭐-03-gagner-xp\n🔨-04-trouver-objet\n🏅-05-gagner-points',
            '2': '⚔-06-combats-et-attaques\n🏞️-07-lieux (Aller à ...)\n🏞️-08-lieux (Explorer lieux)\n🚶🏻-09-trajets\n🧪-10-potions',
            '3': '🌋-11-pve\n🔍-12-rapports\n🤝-13-rencontres\n♥️-14-vie'
        }
        return discord.Embed(
            color=0x00ff00,
            title=f'Page {page}',
            description=pages.get(page, 'Page non trouvée')
        )

async def setup(bot):
    await bot.add_cog(Missions(bot))
