import a2s
import asyncio
from .servers import ServerAddress


class GameServer:
    def __init__(self, region, address, info, players):
        self.region =region
        self.address = address
        self.info = info
        self.players = players


async def server_is_tf2(server_address: ServerAddress):
    info = await a2s.ainfo((server_address.ip, server_address.port))
    return info.app_id == 440


async def get_player_list(server_address: ServerAddress):
    player_list = await a2s.aplayers((server_address.ip, server_address.port))
    return player_list


async def get_server(server_address: ServerAddress):
    try:
        player_list = await a2s.aplayers((server_address.ip, server_address.port))
        info = await a2s.ainfo((server_address.ip, server_address.port))
        return GameServer(server_address.region, server_address, info, player_list)
    except asyncio.exceptions.TimeoutError:
        return None
    except Exception:
        return None


async def check_server(server_address: ServerAddress):
    try:
        is_tf2 = await server_is_tf2(server_address)
        server = None
        if is_tf2:
            server = await get_server(server_address)
        return server
    except Exception:
        return None
