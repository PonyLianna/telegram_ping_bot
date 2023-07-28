class Trusted:
    def __init__(self, trusted_list=None):
        if trusted_list is None:
            trusted_list = []

        self.trusted = trusted_list

    def get_trusted(self):
        return self.trusted

    def set_trusted(self, id: int):
        self.trusted.append(id)
        return self.trusted

    def remove_trusted(self, id: int):
        self.trusted.remove(id)
        return self.trusted
