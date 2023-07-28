from modules.classes.enums.status import Status
from modules.configuration.config import Config

config = Config()


def form_message(status: Status, hostname):
    if status == Status.SUCCESSFULL:
        return f"{config.messages_statuses.successful} {hostname}"
    else:
        return f"{config.messages_statuses.unsuccessful} {hostname}"
