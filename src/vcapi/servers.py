import os.path as path
import json
from collections import namedtuple


ServerAddress = namedtuple("ServerAddress", ["ip", "port", "region"])


def get_data_file_path(filename):
    return path.dirname(__file__) + '\\data\\' + filename


def get_servers_raw():
    with open(get_data_file_path('servers.json'), 'r') as server_json:
        return json.load(server_json)


def get_servers():
    address_list = []

    servers = get_servers_raw()
    regions: dict = servers["regions"]
    game_servers: list = servers["game-servers"]
    for game_server_region in game_servers:
        region = game_server_region["region"]
        region_data = regions[region]
        for block in game_server_region["game-blocks"]:
            address_prefix = block["prefix"]
            for suffix in range(block["ip-range"][0], block["ip-range"][1] + 1):
                address = f'{address_prefix}.{suffix}'
                for port in range(block["port-range"][0], block["port-range"][1]+1):
                    address_list.append(ServerAddress(ip=address, port=port, region=region_data))
    return address_list
