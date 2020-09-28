from dataclasses import dataclass


@dataclass
class Article:
    article_id: str
    article_link: str
    article_title: str
    article_description: str
    image_link: str
    image_description: str
