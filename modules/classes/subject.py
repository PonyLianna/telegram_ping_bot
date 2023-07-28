from abc import abstractmethod, ABC

from modules.classes.subscriber import Subscriber


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
