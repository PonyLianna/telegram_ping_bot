class HostnameConstructor:
    def __init__(self, name: str, address: str, constructor: str = "default"):
        self.name = name
        self.address = address
        self.str_constructor = constructor
        self.constructor: object

    def build_constructor(self):
        pass

