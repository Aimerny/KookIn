from mcdreforged.command.builder.nodes.arguments import GreedyText
from mcdreforged.command.builder.nodes.basic import Literal
from mcdreforged.plugin.server_interface import PluginServerInterface

import kookin.util as util
from kook_api.event import Event
from kookin.config import Config
from kookin.constant import GlobalKey

config: Config


def command_parse(event: Event):
    content = event.content
    channel_id = event.channel_id

    # 同步频道的消息转到服务器
    if channel_id in config.sync_chat_channel:
        util.send_to_sync_channel(content)


def register(server: PluginServerInterface):
    global config
    config = util.get_global(GlobalKey.config)
    # register MCDR command
    server.register_command(
        Literal("!!kk").then(GreedyText("message").runs(send_message))
    )


def send_message(server, ctx):
    player = server.player if server.is_player else "Server"
    message = f'<{player}>{ctx["message"]}'
    util.send_to_sync_channel(message)
    util.send_to_public_channel(message)
