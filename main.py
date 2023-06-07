from __future__ import annotations

import asyncio
import pathlib

import paramiko
from telethon import TelegramClient, events

from classes.singleton import Singleton
from classes.status import Status, form_message
from classes.subject import ConcreteSubject
from classes.subscriber import Subscriber
from config.config import Config

config = Config()

bot = TelegramClient('bot', config.api_id, config.api_hash).start(bot_token=config.bot_token)

k = paramiko.RSAKey.from_private_key_file(
    pathlib.Path(config.pkey_path))
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class MainLoop(metaclass=Singleton):
    subject = ConcreteSubject()
    subject.init_observers(config.subscribers)

    async def start_listen(self):
        while 1:
            await asyncio.sleep(config.sleeping_time)
            try:
                c.connect(hostname=config.hostname, username=config.username, pkey=k)
                await self.subject.listen(Status(1))
            except:
                await self.subject.listen(Status(0))

            finally:
                if c:
                    c.close()


test = MainLoop()


@bot.on(events.NewMessage(pattern='/status'))
async def start(event):
    if MainLoop.subject.status() == Status.SUCCESSFULL:
        await event.respond(f"✅ Connection online for {config.hostname} ✅")
    else:
        await event.respond(f"🆘 Connection offline for {config.hostname} 🆘")


@bot.on(events.NewMessage(pattern='/subscribe'))
async def start(event):
    user_id = event.chat_id
    if not MainLoop.subject.is_attached_by_id(user_id):
        MainLoop.subject.attach(Subscriber(user_id))
        await event.respond('Subscribed')
    else:
        MainLoop.subject.detach_by_id(user_id)
        await event.respond('Unsubscribed')

    raise events.StopPropagation


def main():
    bot.run_until_disconnected()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test.start_listen())
    main()
