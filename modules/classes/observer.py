from abc import abstractmethod, ABC


class Observer(ABC):
    @abstractmethod
    def update(self, subject) -> None:
        pass
