from mcdreforged.plugin.server_interface import PluginServerInterface

from kook_api import KookApi
from kook_api.event import Event
from kookin.config import Config, Data

config: Config
data: Data
kookApi: KookApi


def init(config_, data_, kook_api_):
    global config, data, kookApi
    config = config_
    data = data_
    kookApi = kook_api_


def handle(server: PluginServerInterface, command: str, event: Event):
    if command == 'help':
        # todo help
        pass
    elif command == 'bind':
        # todo bind help
        pass
    elif command == 'whitelist':
        # todo whitelist help
        pass
    elif command == 'list':
        player_list = server.get_plugin_instance("online_player_api").get_player_list()
        message = ''
        bot_group = list(filter(lambda p: p.lower().startswith('bot_'), player_list))
        player_group = list(filter(lambda p: not p.lower().startswith('bot_'), player_list))
        if len(player_list) != 0:
            message += "=== 玩家列表 ===\n"
        for player in player_group:
            message += f'{player}\n'
        message += "=== BOT列表 ===\n"
        for bot in bot_group:
            message += f'{bot}\n'
        message += f"**在线玩家共{len(player_list)}人**\n"
        kookApi.reply(event, message)
