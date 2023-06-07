from classes.observer import Observer
from classes.status import form_message
from classes.subject import ConcreteSubject


class Subscriber(Observer):
    def __init__(self, id: int):
        self.id = id

    async def update(self, subject: ConcreteSubject) -> None:
        message = form_message(subject.status())
        await bot.send_message(self.id, message=message)
