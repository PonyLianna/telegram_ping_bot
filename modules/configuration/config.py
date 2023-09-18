import yaml

from modules.classes.dataclasses.messages import Messages
from modules.classes.dataclasses.subscribed import SubscribedMessages
from modules.classes.singleton import Singleton
from modules.configuration.classes.subscribers import Subscribers
from modules.configuration.classes.trusted import Trusted


class Config(metaclass=Singleton):
    sleeping_time = 60
    config_file_name = "./configuration/config.yaml"
    subscribers = Subscribers()
    trusted = Trusted()

    def __init__(self):
        self.config = self.get_config()

        self.subscribers_file_name = self.config["telegram"]["subscribers_file_name"]
        self.subscribers.file_name = self.subscribers_file_name

        self.subscribers.get_subscribers()

        self.api_id = self.config["telegram"]["api_id"]
        self.api_hash = self.config["telegram"]["api_hash"]

        self.api_hash = str(self.api_hash)

        self.phone = self.config["telegram"]["phone"]
        self.password = self.config["telegram"]["password"]
        self.bot_token = self.config["telegram"]["bot_token"]

        self.ssh = self.config["ssh"]

        self.hostnames = self.ssh["hostnames"]

        self.username = self.ssh["username"]
        self.pkey_path = self.ssh["pkey_path"]

        self.messages = self.config["telegram"]["messages"]

        self.messages_statuses = Messages(
            successful=self.messages["successful"],
            unsuccessful=self.messages["unsuccessful"],
        )

        self.subscribed_messages = SubscribedMessages(
            subscribed=self.messages["subscribed"],
            unsubscribed=self.messages["unsubscribed"],
        )

    def get_config(self):
        with open(self.config_file_name, encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config

    def set_subscribers(self, subscribers):
        return self.subscribers.set_subscribers(subscribers)

    def get_subscribers(self):
        return self.subscribers.get_subscribers()
