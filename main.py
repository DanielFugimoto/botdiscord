from unicodedata import name
import discord
from discord import app_commands
import random

id_do_servidor =  1024709389225037936

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:  
            await tree.sync(guild = discord.Object(id=id_do_servidor))
            self.synced = True
        print(f"{self.user} está online.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id = id_do_servidor), name = 'ola', description ='Olá!') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá tudo bem?", ephemeral = True) 

@tree.command(guild = discord.Object(id = id_do_servidor), name = 'd20', description ='Rola um dado de 20 lados aleatorio') 
async def slash2(interaction: discord.Interaction):
    numero = random.randint(1,20)
    await interaction.response.send_message(f"Número {numero}", ephemeral = False) 

@tree.command(guild = discord.Object(id = id_do_servidor), name = 'regras', description ='Regras do servidor') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Para acessar as regras entre no link:\n https://www.google.com \n Para mais regras ou dúvidas, entre em contato com os administradores", ephemeral = True) 

@tree.command(guild = discord.Object(id = id_do_servidor), name = 'caracoroa', description = 'Cara ou coroa')
async def slash2(interection: discord.Integration):
    res = random.choice(["Cara", "Coroa"])
    await interection.response.send_message(f"Você tirou: {res}", ephemeral = False) 

aclient.run('MTAyNDcxMDU4NTcwMDU4MTQxNg.GzqzsH.R7Ak51YtO1EP9ZJ6k_1YkgX0EE0I9ZU4_EqABI')
