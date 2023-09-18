from __future__ import annotations

import asyncio

from telethon import TelegramClient, events

from modules.classes.main_loop import MainLoop
from modules.classes.subscriber import Subscriber
from modules.configuration.config import Config
from utils.form_message import form_message

config = Config()

bot = TelegramClient("bot", api_id=config.api_id, api_hash=config.api_hash).start(
    bot_token=config.bot_token
)
test = MainLoop(bot=bot, config=config)


@bot.on(events.NewMessage(pattern="/status"))
async def status(event):
    for server in test.get_server_resolver().get_all():
        status = form_message(server.status(), server.get_raw())
        await event.respond(status)


@bot.on(events.NewMessage(pattern="/subscribe"))
async def subscribe(event):
    user_id = event.chat_id
    server = test.get_server_resolver().get_all()[0]
    if not server.is_attached_by_id(user_id):
        server.attach(Subscriber(user_id, bot))
        await event.respond(config.subscribed_messages.subscribed)
    else:
        server.detach_by_id(user_id)
        await event.respond(config.subscribed_messages.unsubscribed)

    raise events.StopPropagation


def main():
    bot.run_until_disconnected()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test.start_listen())
    main()
