from abc import ABC, abstractmethod
from typing import List

from modules.classes.dataclasses.server_config import ServerConfig
from modules.classes.enums.status import Status
from modules.classes.subscriber import Subscriber


class AbstractSubject(ABC):
    _state: int
    _ip: str
    _name: str
    _observers: List[Subscriber]

    @abstractmethod
    def init_observers(self, subscribers_file) -> List[Subscriber]:
        pass

    @abstractmethod
    def get(self) -> ServerConfig:
        pass

    @abstractmethod
    def get_user_ids(self) -> List[str]:
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def edit(self, name, ip):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def attach(self, observer: Subscriber) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Subscriber) -> None:
        pass

    @abstractmethod
    def detach_by_id(self, user_id: int):
        pass

    @abstractmethod
    async def notify(self) -> None:
        pass

    @abstractmethod
    def is_attached(self, observer: Subscriber) -> bool:
        pass

    @abstractmethod
    def is_attached_by_id(self, observer_id: int) -> bool:
        pass

    @abstractmethod
    async def listen(self, status: Status) -> None:
        pass