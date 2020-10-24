import discord
from discord.ext import commands
import datetime as dt
from HLDB_func.HLDB_normal_msg import give_msg
version = '1.0.3'
TOKEN = "SECRET TOKEN"

app = commands.Bot(command_prefix="#")

@app.event # startup partition
async def on_ready():
    game = discord.Game("#도움")
    await app.change_presence(status=discord.Status.online, activity=game)
    print("Logged on as {0},name is helper_loot".format(discord.Client.user))
    print("+-------+--------+")
    print("|command|  user  |")
    print("+-------+--------+")
    print("|startup|  bot   |")

app.remove_command("help") # to use 'help'aliases
@app.command(name="도움", aliases=('help',)) # help partition
async def send_help_msg(ctx, command="help"):
    print("|help({})|{}|".format(command, ctx.message.author))

    embed = discord.Embed(title="\'helper_loot\' 도움말",
                          description=give_msg(command),
                          colour=0x4262F4)

    await ctx.send(embed=embed)

#todo database로 유저의 정보 업데이트
@app.command(name="레식기록", aliases=('r6recode',)) # r6recode partition
async def recode_r6(ctx, result=None, now_rank=None):
    time = dt.datetime.now()
    if result == None or now_rank == None:
        await ctx.send("you give wrong type of input | 잘못된 입력입니다")
        return
    await ctx.send("now time | 현시간{}\n{}\n{}".format(time, result, now_rank))

#todo need fix
@commands.has_role("HLDB_admin") 
@app.command(name="종료", aliases=('shutdown',)) # logout partition
async def shutdown(ctx):
    await ctx.send("logout...")
    await app.logout()

#todo need fix
@shutdown.error
async def shutdown_error(ctx, error): # logout error partition
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("User {0}! don't have permission to use this command | {0}님, 당신은 이 명령을 실행하실 권한이 없습니다.".format(ctx.message.author))

app.run(TOKEN)
