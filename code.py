import discord
from discord.ext import commands

TOKEN = "NzYyOTc3NzgyMTAzODAxODY2.X3xAbg.YShtxxNZrltt4V2BpGy_eOouLIs"

app = commands.Bot(command_prefix="/")

@app.event
async def on_ready():
    game = discord.Game("/도움")
    await app.change_presence(status=discord.Status.online, activity=game)
    print("Logged on as {0},name is helper_loot".format(discord.Client.user))
    print("+-------+--------+")
    print("|command|  user  |")
    print("+-------+--------+")
    print("|startup|  bot   |")
@app.command(name="도움", aliases=('help',))
async def send_help_msg(ctx):
    print("| help  |{}|".format(ctx.message.author))
    help_msg = """                                                      
HELPER LOOT COMMAND
This program is open source | 이프로그램은 오픈소스입니다
you can check  to watch code | 위 사이트로 이동해서 코드를 볼 수 있습니다
====================
+---COMMAND_LIST---+
|     도움(help)    |
| 레식기록(R6recode) |(undeveloped | 개발되지 않음)
+-------------------+
You can check how to use command by \'/?\' at behind of the command | 명령어 뒤에 \'/?\'를 붙임으로써 명령어 이용방법을 확인 할 수 있습니다
If you have inquiries, please DM to 𝓁𝑜𝑜𝓉#0204 | 문의가 있을경우 𝓁𝑜𝑜𝓉#0204로 DM 주세요
"""
    embed = discord.Embed(title="\'helper_loot\' 도움말", description=help_msg)
    await ctx.send(embed=embed)

app.run(TOKEN)
