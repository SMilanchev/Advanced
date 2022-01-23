from .category import Category
from .topic import Topic


class Document:
    tags = []

    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        tags = ", ".join([t for t in self.tags])
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}," \
               f" tags: {tags}"  # care () in tags


