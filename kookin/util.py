import re
from typing import List, Any

from mcdreforged.plugin.server_interface import PluginServerInterface
from mcdreforged.utils.serializer import Serializable

from kook_api import KookApi
from kookin.config import Config, Data
from kook_api.model.send_message import *
from kookin.exceptions import *
from kookin.constant import GlobalKey

config: Config
kookApi: KookApi
data: Data


def init(conf: Config, api: KookApi, data_: Data):
    global config, kookApi, data
    config = conf
    kookApi = api
    data = data_


# === Global Var Get ===
def get_global(key: GlobalKey):
    if key == GlobalKey.config:
        return config
    elif key == GlobalKey.data:
        return data
    elif key == GlobalKey.kookApi:
        return kookApi


# === Config Var ===
def get_all_public_channel_ids() -> List[str]:
    return convert_channel_list_to_ids(config.public_channel)


def get_all_sync_chat_channel_ids() -> List[str]:
    return convert_channel_list_to_ids(config.sync_chat_channel)


def get_all_admin_channel_ids() -> List[str]:
    return convert_channel_list_to_ids(config.admin_channel)


def convert_channel_list_to_ids(channels: List[dict]) -> List[str]:
    channel_ids = []
    for channel_info in channels:
        channel_ids.append(channel_info['channel_id'])
    return channel_ids


# === Message Send ===
def send_to_public_channel(content: str, message_type=MessageType.K_MARKDOWN):
    for channelInfo in config.public_channel:
        kookApi.send_message_to_channel(
            SendMsgReq(target_id=channelInfo['channel_id'], content=content, message_type=message_type)
        )


def send_to_admin_channel(content: str, message_type=MessageType.K_MARKDOWN):
    for channelInfo in config.admin_channel:
        kookApi.send_message_to_channel(
            SendMsgReq(target_id=channelInfo['channel_id'], content=content, message_type=message_type)
        )


def send_to_sync_channel(content: str, message_type=MessageType.K_MARKDOWN):
    for channelInfo in config.sync_chat_channel:
        kookApi.send_message_to_channel(
            SendMsgReq(target_id=channelInfo['channel_id'], content=content, message_type=message_type)
        )


def send_to_all_channel(content: str, message_type=MessageType.K_MARKDOWN):
    send_to_public_channel(content, message_type)
    send_to_admin_channel(content, message_type)
    send_to_sync_channel(content, message_type)


# === Config Edit ===
def save_file(obj: Serializable, file_name: str, server: PluginServerInterface):
    server.save_config_simple(obj, file_name)
