
import asyncio

import a2s

import vcapi.query as query
import vcapi.servers as servers

import json


def query_servers(server_list):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    task_sets = []

    current_task_set = []

    for server in server_list:
        if len(current_task_set) < 500:
            current_task_set.append(query.get_server(server))
        else:
            task_sets.append(list(current_task_set))
            current_task_set = []

    task_sets.append(current_task_set)

    results = []
    for set in task_sets:
        results += loop.run_until_complete(asyncio.gather(*set))

    loop.close()
    return [listing for listing in results if listing != None]


def query_casual_servers():
    server_list = servers.get_servers()
    return query_servers(server_list)


def casual_server_listing():
    return query_casual_servers()


def serialize_server_listing(server_listing):
    server_list = []
    for server in server_listing:
        address = f'{server.address.ip}:{server.address.port}'
        server_item = {"region": server.region, "address": address,
                       'info': {'name': server.info.server_name, 'map': server.info.map_name,
                                'tags': server.info.keywords}, 'players': []}

        for player_object in server.players:
            player = {"name": player_object.name, "score": player_object.score, "duration": player_object.duration,
                      "index": player_object.index}
            server_item['players'].append(player)
        server_list.append(server_item)
    return server_list


def dump_listing_to_file(fd):
    json.dump(serialize_server_listing(casual_server_listing()), fd)
