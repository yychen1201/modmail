from operator import iadd
import discord
from discord.ext import commands 
import os
TOKEN = os.environ['TOKEN']
intent=discord.Intents.all()
client = commands.Bot(command_prefix='/',help_command=None,intents=intent)
@client.event
async def on_ready():
    activity_w = discord.Activity(type=discord.ActivityType.playing, name="傳及回請記得打/回報")
    await client.change_presence(activity=activity_w)
    print('online')
@client.command()
async def 回報(ctx,*,msg):
    A=ctx.author.id
    await ctx.send("感謝您的訊息")
    user_msg = await client.fetch_user(1009412927754866728)
    await user_msg.send(f"回報者<@{A}>(他的id {A} )回報內容:"+msg)
    user_msg = await client.fetch_user(1026305151100788736)
    await user_msg.send(f"回報者<@{A}>(他的id {A} )回報內容:"+msg)
@client.command()
async def 回覆(ctx,id,*,msg):
    if ctx.author==91009412927754866728 or 1026305151100788736 :
        user_msg = await client.fetch_user(id)
        await user_msg.send(msg)
    else:
        return    
client.run(TOKEN)
