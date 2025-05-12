import asyncio
import json

from libs import bot
from libs.loger import aloger


p_ad = "ws://10.61.114.50:2048"
my_app = bot.App(name="LiteLoader",auth_key="caixukun66",uri=p_ad)




@my_app.register("message")
async def handle(ws, send:callable, sender:str, type_:str, content:any, time:str):
    """
    :param ws: Websocket object
    :param send: A fast function which you can use it to send data quickly
    :param sender: sender name
    :param type_:
    :param content:
    :param time:
    :return: None
    """
    if sender == "cxk" and content == "connect success":
        return_data = {"action": "serial_print", "param": {"port": 4, "rate": 115200, "data": f"page 1"}}
        await asyncio.sleep(2) #等待开发板上电完成
        await send(return_data)



@my_app.register("message")
async def handle(ws, send:callable, sender:str, type_:str, content:any, time:str):
    """

    :param ws: Websocket object
    :param send: A fast function which you can use it to send data quickly
    :param sender: sender name
    :param type_:
    :param content:
    :param time:
    :return: None
    """
    if sender == "cxk":
        try:
            if content.get("event_name") == None:
                return
            else:

                return_data = {"action": "serial_print", "param": {"port": 4, "rate": 115200, "data": f"page 1"}}
                await asyncio.sleep(2) #等待开发板上电完成
                await send(return_data)
        except Exception as e:
            pass






note = """
               ______     __     __     ______     ______     ______     ______  
              /\  == \   /\ \  _ \ \   /\  ___\   /\  == \   /\  __ \   /\__  _\ 
              \ \  __<   \ \ \/ ".\ \  \ \ \____  \ \  __<   \ \ \/\ \  \/_/\ \/ 
               \ \_____\  \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
                \/_____/   \/_/   \/_/   \/_____/   \/_____/   \/_____/     \/_/ 
"""



if __name__ == "__main__":
    print(note)
    import plugins.agent as agent
    import plugins.weather as we

    aloger.info(f"""<{agent.INFO["plugin"]}{agent.version}> | {agent.INFO["author"]} | {agent.INFO["description"]}""")
    aloger.info(f"""<{we.INFO["plugin"]}{we.version}> | {we.INFO["author"]} | {we.INFO["description"]}""")
    my_app.run()