from dataclasses import dataclass


@dataclass
class ServerConfig:
    name: str
    ip: str
