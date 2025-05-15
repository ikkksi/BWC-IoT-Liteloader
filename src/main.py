import asyncio
import json

from libs import bot
from libs.loger import aloger
from libs.plm import plm

p_ad = "ws://192.168.13.243:2048"
my_app = bot.App(name="LiteLoader",auth_key="caixukun66",uri=p_ad)


@my_app.register("message")
async def handler(ws, send:callable, sender:str, type_:str, content:any, time:str):
    for call in plm.handle_list:
        if call[1] != type_:
            continue
        await call[0](ws, send, sender, type_, content,time)












note = """
               ______     __     __     ______     ______     ______     ______  
              /\  == \   /\ \  _ \ \   /\  ___\   /\  == \   /\  __ \   /\__  _\ 
              \ \  __<   \ \ \/ ".\ \  \ \ \____  \ \  __<   \ \ \/\ \  \/_/\ \/ 
               \ \_____\  \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
                \/_____/   \/_/   \/_/   \/_____/   \/_____/   \/_____/     \/_/ 
"""



if __name__ == "__main__":



    my_app.run()