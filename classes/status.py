from enum import Enum

from config.config import Config

config = Config()

class Status(Enum):
    UNSUCCESSFUL = 0
    SUCCESSFULL = 1


def form_message(status: Status):
    if status == Status.SUCCESSFULL:
        return f"✅ Connection online for {config.hostname} ✅"
    else:
        return f"🆘 Connection offline for {config.hostname} 🆘"
