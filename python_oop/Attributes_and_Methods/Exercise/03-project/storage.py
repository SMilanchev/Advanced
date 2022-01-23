from typing import List
from .category import Category
from .topic import Topic
from .document import Document


class Storage:
    documents: List[Document]
    categories: List[Category]
    topics: List[Topic]

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        self.topics.append(topic)

    def add_document(self, document: Document):
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        cat_ids = [cat.id for cat in self.categories]
        setattr(self.categories[cat_ids.index(category_id)], 'name', new_name)  # CARE

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topics_ids = [t.id for t in self.topics]
        setattr(self.categories[topics_ids.index(topic_id)], 'topic', new_topic)  # CARE
        setattr(self.categories[topics_ids.index(topic_id)], 'storage_folder', new_storage_folder)  # CARE

    def edit_document(self, document_id: int, new_file_name: str):
        documents_ids = [d.id for d in self.documents]
        setattr(self.documents[documents_ids.index(document_id)], 'file_name', new_file_name)

    def delete_category(self, category_id):
        cat_ids = [c.id for c in self.categories]
        del self.categories[cat_ids.index(category_id)]

    def delete_topic(self, topic_id):
        topic_ids = [t.id for t in self.topics]
        del self.topics[topic_ids.index(topic_id)]

    def delete_document(self, document_id):
        documents_ids = [d.id for d in self.documents]
        del self.documents[documents_ids.index(document_id)]

    def get_document(self, document_id):
        documents_ids = [d.id for d in self.documents]
        document = self.documents[documents_ids.index(document_id)]
        return document

    def __repr__(self):
        documents = list(map(str, self.documents))
        return "\n".join(documents)
