from mcdreforged.plugin.server_interface import PluginServerInterface

from kook_api import KookApi
from kookin.config import Config,Data
from kook_api.event import Event
from kookin.command import single_handler, bind_handler
from kookin.util import get_global, send_to_sync_channel, get_all_sync_chat_channel_ids
from kookin.constant import GlobalKey

config:Config
data:Data
kook_api:KookApi

def init():
    global config, data, kook_api
    config = get_global(GlobalKey.config)
    data = get_global(GlobalKey.data)
    kook_api = get_global(GlobalKey.kookApi)

    #init handlers
    bind_handler.init(config, data, kook_api)
    single_handler.init(config, data, kook_api)

def on_message(server: PluginServerInterface, raw_content:str, event:Event):
    content = event.content.strip()
    if not content.startswith('/'):

        if event.channel_id in get_all_sync_chat_channel_ids():
            exist_user = data.find_user_by_id(event.author_id)
            if exist_user is not None:
                return server.say(f"§7[Kook][{exist_user['username']}]{raw_content}")
            else:
                return send_to_sync_channel(f"*你尚未绑定Id，请使用/bind <id>绑定*")
        else:
            return

    # 检查指令 校验长度
    if len(content) < 2: return
    command_nodes = content[1:].split(' ')
    if len(command_nodes) == 1:
        # 无参指令走single_handler
        return single_handler.handle(server, command_nodes[0], event)
    else:
        if command_nodes[0] == 'bind':
            return bind_handler.handle(server, command_nodes, event)