#インストールしたdiscord.pyを読み込む
import discord
import asyncio
import aiohttp
import subprocess
import functools
import typing
import os
import settings
from typing import Any
from discord.ext import commands

GLOBAL = settings

ID_CHANNEL_TALK = 1044528729747095582
ID_CHANNEL_ROOM = 894574539697176646
ID_CHANNEL_YD = 1082361310207033405
ID_CHANNEL_KIKI = 1073249254421835858
ID_CHANNEL_TEST = 1084812406364053564
ID_CHANNEL_MYCH = 838968840837922829
EMOJI_PIN = '📌' #"Cheonggyecheon"

#intents引数の生成　default:デフォルトのintents
intents = discord.Intents.default()
intents.messages = True
intents.message_content=True

#botコマンドの設定
bot = commands.Bot(command_prefix = '$' , intents = intents)

#接続に必要なオブジェクト生成
client = discord.Client(intents = intents)
parprocess = 0
#起動時の処理
@client.event
async def on_ready():
    #起動時にターミナルに知らせる
    print("ログインしました")

@bot.command()
async def test(ctx, arg):
    print(arg)
    await ctx.send(arg)
    
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
        
#リアクション追加時のイベントハンドラ
@client.event
async def on_raw_reaction_add(payload):
    #リアクションされたメッセージがどのチャンネルのものか確認する
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    
    #対象のチャンネル以外でリアクションがされた場合は無視する
    if channel.id == ID_CHANNEL_TALK or ID_CHANNEL_KIKI: #ID_CHANNEL_TALK or ID_CHANNEL_ROOM or ID_CHANNEL_YD:

        #対象のスタンプであればピン止めし一言
        if payload.emoji.name != EMOJI_PIN:
            print("other2")
            #await channel.send("<:Cheonggyecheon:1070720806264504361>")
            return
    
        await message.pin()
        #await channel.send("<:adult_came:1074293464746962995>")
        text = f'その発言見逃しません！！！'
        await channel.send(text)
        message.content = text
    
#リアクションが消されたときピンを消す
@client.event
async def on_raw_reaction_remove(payload):
    #リアクションされたメッセージがどのチャンネルのものか確認する
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    
    #対象のチャンネル以外でリアクションがされた場合は無視する
    if channel.id == ID_CHANNEL_TALK or ID_CHANNEL_KIKI: #ID_CHANNEL_TALK or ID_CHANNEL_ROOM or ID_CHANNEL_YD:
    
        #対象のスタンプであればピン止めし一言
        if payload.emoji.name != EMOJI_PIN:
            #await channel.send("<:Cheonggyecheon:1070720806264504361>")
            print("other4")
            return
    
        await message.unpin()
        #await channel.send("<:not_adult:1078250973627174943>")
        text = f'もう見た'
        await channel.send(text)
        message.content = text
    
#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #/nekoと発言したらんなおと返す
    if message.content == "おはよ":
        await message.channel.send("おはんよ")
#startと発言したらサーバーを起動する
    if message.content == "start":
        await message.channel.send("サーバーを起動しました！")
        os.system('start.bat')
        return
    if message.content == "close":
        await message.channel.send("サーバーを閉じました！")
        os.system('close.bat')
        return
#Botの起動とDiscordサーバーへの接続

client.run(GLOBAL.TOKEN)