import discord
import asyncio
import aiohttp
from typing import Any
from discord.ext import commands

#mybotのアクセストークンの設定
TOKEN = "MTA4NDcwMTAzNTA4NTQzODk5Ng.GwG_RS.9Dl5K3UDryCFK3sP6CTI8zlZtn6MRTvv4Ay5NU"

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot試運転"),  # "〇〇をプレイ中"の"〇〇"を設定,
)


# 起動時に自動的に動くメソッド
# #03で詳しく説明します
@bot.event
async def on_ready():
    # 起動すると、実行したターミナルに"Hello!"と表示される
    print("Hello!")


# Botが見える場所でメッセージが投稿された時に動くメソッド
@bot.event
async def on_message(message: discord.Message):
    # メッセージ送信者がBot(自分を含む)だった場合は無視する
    if message.author.bot:
        return

    # メッセージが"hello"だった場合、"Hello!"と返信する
    if message.content == 'hello':
        await message.reply("Hello!")
        
# pingコマンドを実装
@bot.command(name="ping", description="pingを返します")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"pong to {ctx.author.mention}")
    
# 挨拶コマンド
@bot.command(name="greeting", description="挨拶を行います")
async def greeting(ctx: discord.ApplicationContext, user: discord.Option(discord.User, "対象のユーザー")):
    await ctx.respond(f"Hi, {user.mention}!")


# Botを起動
bot.run(TOKEN)