
from modules.classes.observer import Observer
from utils.form_message import form_message


class Subscriber(Observer):
    def __init__(self, id: int, send_message):
        self.id = id
        self.send_message = send_message

    async def update(self, subject) -> None:
        message = form_message(subject.status(), subject.config)
        await self.send_message(self.id, message=message)
