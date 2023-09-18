from typing import List

from modules.classes.dataclasses.server_config import ServerConfig
from modules.classes.server.concrete_subject import ConcreteSubject


class Server:
    _servers: List[ConcreteSubject] = []

    def __init__(self):
        pass

    def create_multiple(self, servers: List[ConcreteSubject]):
        for server in servers:
            self._servers.append(server)
        return self._servers

    def create(self, server: ConcreteSubject):
        self._servers.append(server)
        return self._servers

    def _find_by_name(self, name):
        servers = list(filter(lambda x: x.name == name, self._servers))
        if len(servers) == 0:
            raise Exception(f"There's no server with name: {name}")

    def edit(self, name: str, new_config: ServerConfig):
        server: ConcreteSubject = self._find_by_name(name)[0]
        return server.edit(new_config.name, new_config.ip)

    def delete(self, name):
        server = self._find_by_name(name)[0]
        del server

    def get_everything(self):
        server_configs: List[ServerConfig] = []
        for server in self._servers:
            server_configs.append(server.get())
        return server_configs

    def get_all(self):
        return self._servers

    def get_by_user(self, uid: str):
        users_servers = []

        for server in self._servers:
            if uid in server.get_user_ids():
                server_info = server.get()
                users_servers.append(
                    {
                        "ip": server_info.ip,
                        "name": server_info.name,
                        "status": server.status(),
                        "user_id": uid,
                    }
                )

        return users_servers

    def start(self, subscribers):
        self._servers[0].init_observers(subscribers)
