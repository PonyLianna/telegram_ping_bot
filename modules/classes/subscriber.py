
from modules.classes.observer import Observer
from utils.form_message import form_message


class Subscriber(Observer):
    def __init__(self, id: int, bot):
        self.id = id
        self.bot = bot

    async def update(self, subject) -> None:
        message = form_message(subject.status(), subject.config)
        await self.bot.send_message(self.id, message=message)
