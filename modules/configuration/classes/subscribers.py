import json


class Subscribers:
    def __init__(self, file_name: str = ""):
        self.file_name = file_name

    def set_subscribers(self, subscribers):
        with open(self.file_name, "w", encoding="utf-8") as outfile:
            outfile.write(json.dumps(subscribers))
        return subscribers

    def get_subscribers(self):
        with open(self.file_name, "r", encoding="utf-8") as nf:
            subscribers = json.load(nf)
        return subscribers
