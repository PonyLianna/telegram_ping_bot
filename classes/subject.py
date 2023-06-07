import json
from abc import abstractmethod, ABC
from typing import List

from classes.status import Status
from config.config import Config
from main import Subscriber

config = Config()


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Subscriber) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Subscriber) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None

    _observers: List[Subscriber] = []

    def init_observers(self, subscribers_file):
        for i in subscribers_file:
            self._observers.append(Subscriber(i))

    def status(self):
        return Status(self._state)

    def attach(self, observer: Subscriber) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)
        config.set_subscribers([i.id for i in self._observers])

    def detach(self, observer: Subscriber) -> None:
        self._observers.remove(observer)
        config.set_subscribers(self._observers)

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
