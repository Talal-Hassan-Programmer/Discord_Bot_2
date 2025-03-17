import discord

#RULES
Main_Rules = (
    "No spamming\n"
    "No NSFW content\n"
    "No hate speech\n"
    "No personal attacks\n"
    "No sharing personal information\n"
    "No sharing other's personal information\n"
    "No sharing links\n"
    "No sharing links to other servers\n"
    "No sharing links to other social media\n\n"
    "No sharing links to other websites\n"
    "No sharing links to other discord bots\n"
)

#Class for message 
class Help(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) 

        #Creating a button
        Rules = discord.ui.Button(label="Rules", style=discord.ButtonStyle.primary, custom_id="rules_button")

        self.add_item(Rules)
        Rules.callback = self.callback #ADDING CALLBACK The responce of the button

    
    #Responce of the button
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(Main_Rules, ephemeral=True)


    #Embed for the message
    embed = discord.Embed(title="Help", description="Click the buttons below to get help", color=discord.Color.green())