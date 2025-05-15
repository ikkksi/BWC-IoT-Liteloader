import asyncio

from libs.loger import aloger
from libs.plm import plm


INFO = {
    "plugin":"test_demo",
    "author":"Lixeer",
    "version":(1,0,0),
}


@plm.load(care_type="message")
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

@plm.load("message")
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

@plm.load(care_type="message")
async def handle(ws, send:callable, sender:str, type_:str, content:any, time:str):
    aloger.info(f"{sender}")