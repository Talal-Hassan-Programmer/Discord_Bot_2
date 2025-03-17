import discord
from discord import app_commands

import funcs
import funcs.help_1


#MAIN CODE FROM DISCORD DOCS
MY_GUILD = discord.Object(id=1332629729118785629)  # replace with your guild id
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


#SETTING THE BOT AND INTENTS
intents = discord.Intents.default()
client = MyClient(intents=intents)

#ON READY EVENT MAIN EVENT
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

#COMMANDS  (hello)
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

#COMMANDS  (hello)
@client.tree.command()
async def help(interaction: discord.Interaction):
    """Says hello!"""
    view = funcs.help_1.Help
    embed = view.embed
    await interaction.response.send_message(view=view(),embed=embed)



#RUNNING THE BOT
client.run("MTMzNzcwNjM0MDkxNDY5MjEzNg.GA-VDY.PyzYKcPnbpIAi8NjgXOFY_dCuOeIWcUivvKkoc")
