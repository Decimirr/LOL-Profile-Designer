import discord, asyncio, os, sys
from discord.ext import commands
from LOLcard import lolcard

client = discord.Client()
token_file = open("token.txt", "r", encoding="utf-8")
token = token_file.read()

game = discord.Game("인쇄 중")
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game)

help_embed = discord.Embed(title=f"인쇄기 명령어 목록", color=0x62c1cc)
help_embed.add_field(name=f"!카드 [솔랭/자랭/롤체] [롤 닉네임]\"", value=f"해당 유저를 한국 서버에서 찾아서 티어 카드를 출력합니다.", inline=False)
help_embed.add_field(name=f"이 줄은 왜 있나요?", value=f"한 줄이면 목록이 아니잖아", inline=False)



@bot.event
async def on_ready():
    print('온라인')


@bot.command()
async def 인쇄기(ctx, *args):
    await ctx.send(embed=help_embed)


@bot.command()
async def 카드(ctx, *args):
    if len(args) == 0:
        await ctx.send(embed=help_embed)
    else:
        nick = "".join(args[x] + " " for x in range(1, len(args)))
        arr = lolcard.create_card(nick.rstrip(), args[0])
        if not arr:
            await ctx.send(embed=help_embed)
        file = discord.File(fp=arr, filename="card.png")
        await ctx.send(file=file)


bot.run(token)

