import json

from libs.bot import register

version = (1,0,0)

INFO = {
    "plugin":"on_gpio_write",
    "author":"holtek",
    "version":version,
    "description":"When listening to the GPIO input, GPIO is output",
}

@register(type_="message")
async def handle(ws, send:callable, sender:str, type_:str, content:any, time:str):
    """
    :param ws: Websocket object
    :param send: A fast function which you can use it to send data quickly
    :param sender: sender name
    """
    if sender == "cxk" and content.get("event_name") == "GPIO_input":  #只对设备名称为cxk的感兴趣
        return_data = {"action": "GPIO_write", "param": {"pin": 12, "status":"LOW"}} #12号引脚设置为低电平，点亮LED
        await send(return_data)
        """
        await ws.send(json.dumps({
                        "sender":"cxk/plugins_xxxx",
                         "type":"message",
                         "content":return_data,
                         "time":"xxxx-xx-xx-xx-xx"}))
        """
        #也可以使用ws对象发送元数据