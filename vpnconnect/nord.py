import json
import operator
from typing import Dict

import requests

from .connection_manager import Server


def find_server(country: str) -> Server:
    print("Retrieving NordVPN server list")

    response = requests.get("https://nordvpn.com/api/server")
    server_data = json.loads(response.text)
    servers = [__create_server(d) for d in server_data if d["flag"].lower() == country]
    servers.sort(key=operator.attrgetter("load"))

    return servers[0]


def __create_server(data: Dict) -> Server:
    return Server(
        country=data["flag"].lower(),
        domain=data["domain"],
        load=data["load"]
    )
