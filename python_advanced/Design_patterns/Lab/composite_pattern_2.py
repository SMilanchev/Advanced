class Component:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def move(self, new_path):
        new_folder = self.get_path()

    @staticmethod
    def get_path(path):
        names = path.split('/')[1:]
        node = Folder('/')
        for name in names:
            node = name.children[name]
        return node


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child


class File:
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents


