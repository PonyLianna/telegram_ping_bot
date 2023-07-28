import asyncio
import pathlib

import paramiko

from modules.classes.enums.status import Status
from modules.classes.server.concrete_subject import ConcreteSubject
from modules.classes.server.server import Server
from modules.classes.singleton import Singleton


class MainLoop(metaclass=Singleton):
    def __init__(self, config, bot):
        self.config = config
        self.bot = bot

        self.k = paramiko.RSAKey.from_private_key_file(pathlib.Path(config.pkey_path))
        self.c = paramiko.SSHClient()
        self.c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.server = Server()
        subscribers = [i for i in self.config.subscribers]

        addresses = [ConcreteSubject(i, self.bot.send_message)
                     for i in self.config.hostnames]

        self.server.create_multiple(addresses)
        self.server.start(subscribers)

    def get_server_resolver(self):
        return self.server

    async def start_listen(self):
        while 1:
            await asyncio.sleep(self.config.sleeping_time)

            for iter_server in self.server.get_all():
                try:
                    self.c.connect(hostname=iter_server.get().ip, username=self.config.username, pkey=self.k)
                    await iter_server.listen(Status(1))
                except:
                    await iter_server.listen(Status(0))

                finally:
                    if self.c:
                        self.c.close()
