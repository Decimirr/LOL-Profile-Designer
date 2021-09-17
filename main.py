import discord, asyncio, os, sys
from discord.ext import commands
from LOLcard import lolcard

client = discord.Client()
token_file = open("token.txt", "r", encoding="utf-8")
token = token_file.read()

game = discord.Game("인쇄 중")
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game)

help_embed = discord.Embed(title=f"프린터 명령어 목록", color=0x62c1cc)
help_embed.add_field(name=f"!프린터 [솔랭/자랭] \"롤 닉네임\"", value=f"해당 유저를 한국 서버에서 찾아서 티어 카드를 출력합니다. 솔랭 및 자랭 옵션은 비워 둘 수 있으며, "
                                                           f"이 경우 솔랭을 우선하여 출력합니다.", inline=False)
help_embed.add_field(name=f"이 줄은 왜 있나요?", value=f"기념으로..", inline=False)



@bot.event
async def on_ready():
    print('온라인')


@bot.command()
async def 프린터(ctx, *args):
    if len(args) == 0:
        await ctx.send(embed=help_embed)
    elif len(args) == 1:
        arr = lolcard.create_card(args[0])
        file = discord.File(fp=arr, filename="card.png")
        await ctx.send(file=file)
    elif len(args) == 2:
        arr = lolcard.create_card(args[1], args[0])
        if not arr:
            await ctx.send(embed=help_embed)
        file = discord.File(fp=arr, filename="card.png")
        await ctx.send(file=file)

bot.run(token)

