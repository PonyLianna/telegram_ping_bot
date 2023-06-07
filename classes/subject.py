from abc import abstractmethod, ABC
from typing import List

from classes.status import Status, form_message
from classes.subscriber import Subscriber
from config.config import Config

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


