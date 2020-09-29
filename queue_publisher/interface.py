from typing import List

from parsers import Article


class IPublisher:
    async def connect(self):
        raise NotImplementedError

    async def send_article(self, article: Article, queue_name: str):
        raise NotImplementedError

    async def send_batch_articles(self, articles: List[Article], queue_name: str):
        raise NotImplementedError
