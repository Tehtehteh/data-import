import logging
import asyncio

from typing import Optional, List
from aiormq import connect, Connection
from parsers.types import Article


logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)


class RMQPublisher:
    def __init__(self, conn_string: str):
        self.conn_string = conn_string
        self.connection: Optional[Connection] = None

    async def connect(self):
        assert self.connection is None
        logger.info("Connecting to %s RMQ instance.", self.conn_string)
        self.connection = await connect(self.conn_string)
        # self.connection.

    @property
    def started(self):
        return self.connection and self.connection.is_opened

    @property
    def stopped(self):
        return not self.started

    async def send_article(self, article: Article, queue_name: str):
        logging.info("Sending %s article to %s queue", article, queue_name)
        channel = await self.connection.channel()
        confirmation = await channel.basic_publish(body=article.to_bytes(),
                                                   routing_key=queue_name)
        logging.info("Send successful, confirmation: %s", confirmation)

    async def send_batch_articles(self, articles: List[Article],
                                  queue_name: str):
        futures = [self.send_article(article, queue_name) for article in articles]
        await asyncio.gather(*futures)

    def __del__(self):
        if self.started:
            asyncio.ensure_future(self.connection.close())


if __name__ == '__main__':
    test_rmq_conn_string = "amqp://guest:guest@localhost"

    async def test_publish():
        publisher = RMQPublisher(test_rmq_conn_string)
        article = Article("qeq", "qeq", "", "", "", "", source="QWA")
        await publisher.connect()
        await publisher.send_article(article, "article")

    asyncio.get_event_loop().run_until_complete(test_publish())
    asyncio.get_event_loop().run_forever()
