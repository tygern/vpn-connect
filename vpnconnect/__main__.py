import argparse

from .connection_manager import ConnectionManager
from .nord import find_server


def main():
    parser = argparse.ArgumentParser(description="Connect to NordVPN servers")
    parser.add_argument("country", type=str)

    args = parser.parse_args()

    server = find_server(args.country.lower())

    manager = ConnectionManager(server)

    manager.prepare_connection()
    manager.open_connection()


if __name__ == '__main__':
    main()
