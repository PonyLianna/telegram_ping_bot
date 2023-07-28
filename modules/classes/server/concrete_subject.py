from abc import ABC, abstractmethod
from typing import List

from modules.classes.dataclasses.server_config import ServerConfig
from modules.classes.enums.status import Status
from modules.classes.server.abstract_concrete_subject import AbstractSubject
from modules.classes.subject import Subject
from modules.classes.subscriber import Subscriber
from modules.configuration.config import Config

global_config = Config()


class ConcreteSubject(Subject, AbstractSubject):
    _state: int = None
    _ip = ""
    _name = ""
    _observers: List[Subscriber] = []

    def __init__(self, config, bot):
        # self.server_config = server_config
        self.config = config
        self.bot = bot

        self._name = list(config.keys())[0]
        self._ip = config[self._name]["address"]

    def init_observers(self, subscribers_file) -> List[Subscriber]:
        for i in subscribers_file:
            self._observers.append(Subscriber(i, self.bot))
        return self._observers

    def get(self) -> ServerConfig:
        return ServerConfig(self._name, self._ip)

    def get_raw(self):
        return self.config

    def get_user_ids(self) -> List[str]:
        return list(map(lambda x: x.id, self._observers))

    def get_status(self):
        return self._state

    def edit(self, name, ip):
        self._ip = ip
        self._name = name
        return self

    def status(self):
        return Status(self._state)

    def attach(self, observer: Subscriber) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)
        global_config.set_subscribers([i.id for i in self._observers])

    def detach(self, observer: Subscriber) -> None:
        self._observers.remove(observer)
        global_config.set_subscribers(self._observers)

    def detach_by_id(self, user_id: int):
        user = list(filter(lambda x: x.id == user_id, self._observers))[0]
        self.detach(user)

    async def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            await observer.update(self)

    def is_attached(self, observer: Subscriber) -> bool:
        if observer in self._observers:
            return True
        return False

    def is_attached_by_id(self, observer_id: int) -> bool:
        if len(list(filter(lambda x: x.id == observer_id, self._observers))) > 0:
            return True
        return False

    async def listen(self, status: Status) -> None:
        if self._state != status.value:
            print("\nSubject: I'm doing something important.")
            self._state = status.value

            print(f"Subject: My state has just changed to: {self._state}")
            await self.notify()
        else:
            print(f"Subject: My state hasn't changed")
