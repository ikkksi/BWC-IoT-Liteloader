import json
import websockets
import asyncio
from libs.loger import aloger
class App:
    def __init__(self,uri,auth_key,name):
        self.auth_key = auth_key
        self.uri = uri
        self.headers = {"X-Auth-Key":self.auth_key,"Device-Name":name}
        self.name = name

        self._callback_list = []

    async def _on_receive(self,websocket):
        while True:

            try:
                response = await websocket.recv()
                response = json.loads(response)
                aloger.info(response)


                async def send(content):
                    msg={"sender":self.name,
                         "type":"message",
                         "content":content,
                         "time":"xxxx-xx-xx-xx-xx"}
                    await websocket.send(json.dumps(msg))


                for i in self._callback_list:
                    if i[0] == response["type"]:
                        await i[1](websocket,send,**response)



            except websockets.ConnectionClosed:
                aloger.warn("Connection with server closed")
                break

    async def _start(self):
        async with websockets.connect(self.uri, extra_headers=self.headers) as websocket:
            # 启动接收消息的任务
            receive_task = asyncio.create_task(self._on_receive(websocket))

            # 等待任务完成
            await asyncio.gather(receive_task)

    def register(self,event:str):

        def rg(callback_func):
            self._callback_list.append((event,callback_func))
        return rg

    def run(self):
        aloger.info(f"Bot {self.name} is running in Server {self.uri}")
        asyncio.run(self._start())


