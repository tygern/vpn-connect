import os
import subprocess
from dataclasses import dataclass

from .password_manager import nord_password, nord_username


@dataclass(frozen=True)
class Server(object):
    country: str
    domain: str
    load: int


class ConnectionManager(object):

    def __init__(self, server: Server) -> None:
        self.__connection = f"{server.domain}.tcp"

    def prepare_connection(self):
        if self.__connection_exists():
            print(f"Connection to {self.__connection} already exists.")
            return True

        self.__create_connection()
        self.__add_username_to_connection()

    def open_connection(self):
        print(f"Opening connection to {self.__connection}.")

        subprocess.run(
            ["nmcli", "connection", "up", self.__connection, "--ask"],
            check=True,
            input=nord_password().encode()
        )

    def __connection_exists(self) -> bool:
        result = subprocess.run(
            ["nmcli", "-t", "connection", "show", self.__connection],
            capture_output=True
        )

        return result.returncode == 0

    def __add_username_to_connection(self):
        print(f"Adding NordVPN username to connection {self.__connection}.")

        subprocess.run(
            ["nmcli", "connection", "modify", self.__connection, "+vpn.data", f"username={nord_username()}"],
            check=True
        )

    def __create_connection(self):
        print(f"Creating connection to {self.__connection}.")
        subprocess.run(
            ["nmcli", "connection", "import", "type", "openvpn", "file",
             os.path.expanduser(f"~/vpn/{self.__connection}.ovpn")],
            check=True
        )
