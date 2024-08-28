import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

class Regime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='régime', description="Affiche l'aide sur les régimes des familiers selon leur rareté")
    async def regime(self, interaction: discord.Interaction):
        user = interaction.user
            # Vérification des rôles
        if not any(role.name in ['role1', 'role2'] for role in user.roles): #Vérifie que l'utilisateur a l'un des rôles spécifiés (Les rôles doivent être écrit comme ceci : 'Role1', 'Role2' ect)
            await interaction.response.send_message(
                f"{user.mention}, vous n'avez pas les rôles requis pour utiliser cette commande.", ephemeral=True)
            return
        embed = discord.Embed(
            color=0x00ff00,
            title='Menu des régimes',
            description='Choisissez le niveau de rareté du familier via les boutons ci-dessous :'
        )
        
        view = self.create_buttons_view()
        await interaction.response.send_message(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.component:
            custom_id = interaction.data['custom_id']

            if custom_id == 'regime_close':
                await interaction.response.defer()
                await interaction.message.delete()

            elif custom_id in ['regime_1star', 'regime_2stars', 'regime_3stars', 'regime_4stars', 'regime_5stars']:
                await self.handle_star_interaction(interaction, custom_id)

    async def handle_star_interaction(self, interaction: discord.Interaction, custom_id: str):
        star_map = {
            'regime_1star': ('⭐', 
            "🐔 Poule / Coq : **herbivore**\n"
            "🐦 Oiseau : **herbivore**\n"
            "🐢 Tortue : **herbivore**\n"
            "🐍 Serpent : **carnivore**\n"
            "🐎 Cheval : **herbivore**\n"
            "🐩 Caniche : **carnivore**\n"
            "🐱 Chat : **carnivore**\n"
            "🐈‍⬛ Chat Noir : **carnivore**\n"
            "🐭 Souris : **tout**\n"
            "🦎 Lézard : **carnivore**\n"
            "🐰 Lapin : **herbivore**\n"
            "🐖 Cochon : **herbivore**\n"
            "🦆 Canard : **herbivore**\n"
            "🐄 Vache : **herbivore**\n"
            "🐹 Hamster : **herbivore**\n"
            "⛄ Bonhomme de Neige : **herbivore**\n"
            "🐶 Chien : **carnivore**\n"
            "🐏 Bélier / Mouton : **herbivore**\n"
            "🐐 Chèvre / Bouc : **herbivore**\n"
            "🦃 Dindon : **herbivore**\n"
            "🐟 Poisson : **tout**\n"),

            'regime_2stars': ('⭐⭐', 
            "🦛 Hippopotame : **herbivore**\n"
            "🦙 Lama : **herbivore**\n"
            "🦔 Hérisson : **tout**\n"
            "🦨 Putois : **carnivore**\n"
            "🦡 Blaireau : **tout**\n"
            "🦇 Chauve-souris : **carnivore**\n"
            "🦫 Castor : **herbivore**\n"
            "🐿️ Tamia : **herbivore**\n"
            "🦥 Paresseux : **herbivore**\n"
            "🐺 Loup : **carnivore**\n"
            "🦩 Flamant Rose : **tout**\n"
            "🦭 Otarie : **carnivore**\n"
            "🦝 Raton Laveur : **tout**\n"
            "🐨 Koala : **herbivore**\n"
            "🐸 Grenouille : **herbivore**\n"
            "🐻 Ours : **carnivore**\n"
            "🦊 Renard : **carnivore**\n"
            "🦉 Hibou : **carnivore**\n"
            "🦢 Cygne : **herbivore**\n"
            "🐧 Pingouin : **carnivore**\n"
            "🐒 Singe : **herbivore**\n"
            "🐗 Sanglier : **tout**\n"
            "🪼 Méduse : **tout**\n"
            "🦐 Crevette : **tout**\n"),

            'regime_3stars': ('⭐⭐⭐', 
            "🦓 Zèbre : **herbivore**\n"
            "🦏 Rhinocéros : **herbivore**\n"
            "🦘 Kangourou : **herbivore**\n"
            "🦒 Girafe : **herbivore**\n"
            "🦚 Paon : **herbivore**\n"
            "🐘 Éléphant : **herbivore**\n"
            "🐙 Poulpe : **tout**\n"
            "🐫 Chameau : **herbivore**\n"
            "🐊 Crocodile : **carnivore**\n"
            "🐪 Dromadaire : **herbivore**\n"
            "🦦 Loutre : **carnivore**\n"
            "🦜 Perroquet : **tout**\n"
            "🐻‍❄️ Ours Polaire : **carnivore**\n"
            "🐼 Panda : **herbivore**\n"
            "🦂 Scorpion : **carnivore**\n"
            "🐡 Poisson globe : **tout**\n"
            "🐋 Baleine : **tout**\n"),

            'regime_4stars': ('⭐⭐⭐⭐', 
            "🦣 Mammouth : **herbivore**\n"
            "🕊️ Colombe : **herbivore**\n"
            "🐧 Manchot : **tout**\n"
            "🦅 Aigle : **carnivore**\n"
            "🐆 Léopard : **carnivore**\n"
            "⛄ Bonhomme de Neige : **herbivore**\n"
            "🦁 Lion : **carnivore**\n"
            "🐅 Tigre : **carnivore**\n"
            "🦤 Dodo : **herbivore**\n"
            "🦈 Requin : **tout**\n"
            "🦞 Homard : **tout**\n"
            "🐬 Dauphin : **tout**\n"),

            'regime_5stars': ('⭐⭐⭐⭐⭐', 
            "🦖 T-Rex : **carnivore**\n"
            "🟣 Stitch/Angel : **tout**\n"
            "🦄 Licorne : **tout**\n"
            "🐉 Dragon : **carnivore**\n"
            "👽 Alien : **tout**\n"
            "🦆 Canard Écarlate : **herbivore**\n"
            "🐠 Poisson tropical : **tout**\n"
            "🐳 Baleine : **tout**")
        }

        star, description = star_map[custom_id]
        embed = discord.Embed(
            color=0x00ff00,
            title=f'Rareté {star}',
            description=description
        )
        
        view = self.create_buttons_view()
        await interaction.response.edit_message(embed=embed, view=view)

    def create_buttons_view(self):
        view = View()
        view.add_item(Button(style=discord.ButtonStyle.primary, label='⭐', custom_id='regime_1star'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='⭐⭐', custom_id='regime_2stars'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='⭐⭐⭐', custom_id='regime_3stars'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='⭐⭐⭐⭐', custom_id='regime_4stars'))
        view.add_item(Button(style=discord.ButtonStyle.primary, label='⭐⭐⭐⭐⭐', custom_id='regime_5stars'))
        view.add_item(Button(style=discord.ButtonStyle.danger, label='Fermer', custom_id='regime_close'))
        
        return view

async def setup(bot):
    await bot.add_cog(Regime(bot))
