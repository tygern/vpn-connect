import json
import subprocess


def nord_username() -> str:
    print("Fetching NordVPN username")

    return __fetch_info("username")


def nord_password() -> str:
    print("Fetching NordVPN password")

    return __fetch_info("password")


def __fetch_info(name: str) -> str:
    credentials = subprocess.check_output(["op", "get", "item", "NordVPN"])
    fields = json.loads(credentials)["details"]["fields"]

    return [f["value"] for f in fields if f.get("designation") == name][0]
