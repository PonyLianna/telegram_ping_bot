from abc import abstractmethod, ABC


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject) -> None:
        """
        Receive update from subject.
        """
        pass
