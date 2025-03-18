import discord
from discord import app_commands

import funcs, funcs.help_1


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
intents = discord.Intents.all()
client = MyClient(intents=intents)

#ON READY EVENT MAIN EVENT
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

#Event to assine roles to new members and send a welcome message
@client.event
async def on_member_join(member):
    channel = client.get_channel(1351621585030615151)  #REplace the ID with the channel you want the message to send in

    embed = discord.Embed(
        title=f"Welcome **{member.mention}** !",
        description="Welcome to the server! We hope you enjoy your stay here!",
        color=discord.Color.green()
        )

    role = discord.utils.get(member.guild.roles, name="Member")

    await member.add_roles(role)
    await channel.send(embed=embed)




#COMMANDS  (HELLO)
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

#COMMANDS  (HELP)
@client.tree.command()
async def help(interaction: discord.Interaction):
    """HELP!"""
    view = funcs.help_1.Help
    embed = view.embed
    await interaction.response.send_message(view=view(),embed=embed)



#RUNNING THE BOT
client.run("MTMzNzcwNjM0MDkxNDY5MjEzNg.GA-VDY.PyzYKcPnbpIAi8NjgXOFY_dCuOeIWcUivvKkoc")
