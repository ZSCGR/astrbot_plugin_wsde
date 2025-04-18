import astrbot.api.message_components as Comp
from astrbot.api.all import *
from astrbot.api.event import filter, AstrMessageEvent
import random
import os

@filter.command("wsde")
async def wsde(self, event: AstrMessageEvent):
    chain = [
        Comp.At(qq=event.get_sender_id()), # At 消息发送者
        Comp.Plain("来看这个图："), 
        Comp.Image.fromURL("https://tc.chgr.cc/raw/mc/%E5%A4%B4%E5%9B%BE.png"), # 从 URL 发送图片
        Comp.Image.fromFileSystem("/opt/koishi/vvilxo.png"),# 从本地文件目录发送图片
        Comp.Plain("这是一个图片。"),# 暂时只接受 wav 格式，其他格式请自行转换
        Comp.Record(file='/opt/koishi/戳一下.wav', url='/opt/koishi/戳一下.wav')
    ]
    yield event.chain_result(chain)