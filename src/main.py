import json

from libs import bot,loger
from libs.loger import aloger

p_ad = "ws://127.0.0.1:2048"
my_app = bot.App(name="loader",auth_key="caixukun66",uri=p_ad)




#默认串口设备


@my_app.register("message")
async def sample(ws,send,sender,type,content,time):
    if type == "message":
        await send(f"hi {sender}")

@my_app.register("message")
async def sample(ws,send,sender,type,content,time):
    if type == "message":

        print(content.get("pack"))



note = """
               ______     __     __     ______     ______     ______     ______  
              /\  == \   /\ \  _ \ \   /\  ___\   /\  == \   /\  __ \   /\__  _\ 
              \ \  __<   \ \ \/ ".\ \  \ \ \____  \ \  __<   \ \ \/\ \  \/_/\ \/ 
               \ \_____\  \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
                \/_____/   \/_/   \/_/   \/_____/   \/_____/   \/_____/     \/_/ 
"""



if __name__ == "__main__":
    print(note)
    my_app.run()