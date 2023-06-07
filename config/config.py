import json

import yaml

from classes.singleton import Singleton


class Config(metaclass=Singleton):
    sleeping_time = 60
    config_file_name = './config/config.yaml'

    def __init__(self):
        self.config = self.get_config()
        self.subscribers_file_name = self.config['telegram']['subscribers_file_name']
        self.subscribers = self.get_subscribers()

        self.api_id = self.config['telegram']['api_id']
        self.api_hash = self.config['telegram']['api_hash']

        self.api_hash = str(self.api_hash)

        self.phone = self.config['telegram']['phone']
        self.password = self.config['telegram']['password']
        self.bot_token = self.config['telegram']['bot_token']

        self.ssh = self.config['ssh']

        self.hostname = self.ssh['hostname']
        self.username = self.ssh['username']
        self.pkey_path = self.ssh['pkey_path']

    def get_config(self):
        with open(self.config_file_name) as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)
        return config

    def set_subscribers(self, subscribers):
        with open(self.subscribers_file_name, "w", encoding="utf-8") as outfile:
            outfile.write(json.dumps(subscribers))

    def get_subscribers(self):
        with open(self.subscribers_file_name, "r", encoding="utf-8") as nf:
            subscribers = json.load(nf)
        return subscribers
