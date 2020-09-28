import pickle

from dataclasses import dataclass


@dataclass
class Article:
    article_id: str
    article_link: str
    article_title: str
    article_description: str
    image_link: str
    image_description: str
    source: str

    def __repr__(self):
        return f'Article(id={self.article_id}, source={self.source})'

    def to_bytes(self):
        return pickle.dumps(self)
