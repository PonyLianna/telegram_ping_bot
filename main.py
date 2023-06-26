from __future__ import annotations

import asyncio
import pathlib

import paramiko
from telethon import TelegramClient, events

from classes.concrete_subject import ConcreteSubject
from classes.enums.status import Status
from classes.form_message import form_message
from classes.singleton import Singleton
from classes.subscriber import Subscriber
from config.config import Config

config = Config()

bot = TelegramClient('bot', api_id=config.api_id, api_hash=config.api_hash).start(bot_token=config.bot_token)

k = paramiko.RSAKey.from_private_key_file(pathlib.Path(config.pkey_path))
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class MainLoop(metaclass=Singleton):
    subject = ConcreteSubject(config, bot)
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
    status = form_message(MainLoop.subject.status())
    await event.respond(status)


@bot.on(events.NewMessage(pattern='/subscribe'))
async def start(event):
    user_id = event.chat_id
    if not MainLoop.subject.is_attached_by_id(user_id):
        MainLoop.subject.attach(Subscriber(user_id, bot))
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
