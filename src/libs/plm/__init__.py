"""
plm -> plugins manager
"""
import importlib
import os

from libs.loger import aloger

class PluginsLoader:
    def __init__(self, path:str = "plugins"):
        self.path = path
        self.plugins = []  #这个用来存放插件
        self.plugins_map:dict = {}
        self.handle_list = [] #这个用来存放处理函数，一个插件内可能有多个处理函数
    def _load(self,module):
        """
        将插件对象传递到其他访问结构
        :return:
        """

        pass

    def init(self):

        dir = os.listdir(self.path)
        self.plugins = [os.path.splitext(filename) for filename in dir if filename !="__pycache__"]
        self.plugins = [i[0] for i in self.plugins]

        for plugin in self.plugins:

            m = importlib.import_module(f"{self.path}.{plugin}")
            try:
                self.plugins_map[m.INFO["plugin"]] = m
                aloger.info(f"""插件{m.INFO["plugin"]}<{m.INFO["version"]}> | 作者{m.INFO["author"]}""")
            except:
                aloger.warn(f"插件{m.__name__}未提供必要字段，但依旧被加载")


    def load(self,care_type:str ,callback=None ,**kwargs):


        if callback is not None:
            self.handle_list.append((callback,care_type))
            return callback


        def _(func):
            self.handle_list.append((func,care_type))
            return func

        return _


plm = PluginsLoader()
plm.init()