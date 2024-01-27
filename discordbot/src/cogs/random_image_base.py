import aiohttp
from typing import Any
import discord
from discord.ext import commands
from src.utils import message

class RandomImageBaseCog(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        
    async def send_image(self, channel: discord.channel, url: str, **kwargs: Any) -> None:
        """APIから画像URLを取得しchannelに送信する"""
        json = await self.fetch_url(url , **kwargs)
        image_url = self.get_image_url_from_json(json)
        await message.send_image(channel , image_url)
        
    async def fetch_url(self, url: str, **kwargs: Any) ->Any:
        """URLをfetchしjsonを返す"""
        async with aiohttp.ClientSession(raise_for_status = True) as session:
            async with session.get(url, **kwargs) as response:
                json = await response.json()
                return json
            
    def get_image_url_from_json(self,json: Any) -> str:
        """レスポンスのjsonから画像URLを返す"""
        raise NotImplementedError