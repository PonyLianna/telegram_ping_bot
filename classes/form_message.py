from classes.enums.status import Status
from config.config import Config

config = Config()


def form_message(status: Status):
    if status == Status.SUCCESSFULL:
        return config.messages_statuses.successful
    else:
        return config.messages_statuses.unsuccessful
