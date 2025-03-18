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
    "No sharing links to other social media\n"
    "No sharing links to other websites\n"
    "No sharing links to other discord bots\n"
)


#INFO
info = (
    "**OWNER [Talal Hassan]**\n"
    "**STATUS [development]**\n"
)



#Class for message 
class Help(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) 

        #Creating a button(RULES)
        Rules = discord.ui.Button(label="Rules", style=discord.ButtonStyle.primary, custom_id="rules_button")

        self.add_item(Rules)
        Rules.callback = self.callback_RULES #ADDING CALLBACK The responce of the button (RULES)


        #Creating a button I(INFO)
        Info = discord.ui.Button(label="INFO", style=discord.ButtonStyle.primary, custom_id="info_button")

        self.add_item(Info)
        Info.callback = self.callback_INFO #ADDING CALLBACK The responce of the button (INFO)

    
    #Responce of the button (RULES)
    async def callback_RULES(self, interaction: discord.Interaction):
        await interaction.response.send_message(Main_Rules, ephemeral=True)

    #Responce of the button (INFO)
    async def callback_INFO(self, interaction: discord.Interaction):
        await interaction.response.send_message(info, ephemeral=True)


    #Embed for the message
    embed = discord.Embed(title="Help", description="Click the buttons below to get help", color=discord.Color.green())