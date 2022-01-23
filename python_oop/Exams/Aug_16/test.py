class God: ### SINGLETON
    _instance = None

    def __init__(self):
        assert God._instance is None
        God._instance = self
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            return cls()
        return cls._instance

    def pray(self):
        return 'Praying...'

god_of_pesho = God.get_instance()
god_of_ivan = God.get_instance()
print(god_of_pesho)
print(god_of_ivan)

class GodProxy:
    def __init__(self, god):
        self.__god = god

    def pray(self):
        return self.__god.pray()



god_proxy = GodProxy(God.get_instance())
print(god_proxy.pray())