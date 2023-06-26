from classes.form_message import form_message
from classes.observer import Observer


class Subscriber(Observer):
    def __init__(self, id: int, bot):
        self.id = id
        self.bot = bot

    async def update(self, subject) -> None:
        message = form_message(subject.status())
        await self.bot.send_message(self.id, message=message)
