import discord
from discord.ext import commands
import datetime as dt
from HLDB_func.HLDB_normal_msg import give_msg

TOKEN = "SECRET TOKEN"

app = commands.Bot(command_prefix="#")

@app.event
async def on_ready():
    game = discord.Game("#도움")
    await app.change_presence(status=discord.Status.online, activity=game)
    print("Logged on as {0},name is helper_loot".format(discord.Client.user))
    print("+-------+--------+")
    print("|command|  user  |")
    print("+-------+--------+")
    print("|startup|  bot   |")

@app.command(name="도움")
async def send_help_msg(ctx, command="help"):
    print("| help({})  |{}|".format(command, ctx.message.author))

    if command == "help":
        embed = discord.Embed(title="\'helper_loot\' 도움말", description=give_msg("help"))
    elif command == "레식기록" or command == "r6recode":
        embed = discord.Embed(title="\'helper_loot\' 도움말", description=give_msg("r6recode"))
    await ctx.send(embed=embed)

@app.command(name="레식기록")
async def recode_r6(ctx, result, now_rank):
    #todo database로 유저의 정보 업데이트
    time = dt.datetime.now()
    await ctx.send("now time | 현시간{}\n{}\n{}".format(time, result, now_rank))

app.run(TOKEN)
