import asyncio
import logging
import aiohttp

from config import Config
from typing import Optional, List
from queue_publisher import IPublisher
from parsers import RSSFeed

logger = logging.getLogger(__name__)


class Application:

    def __init__(self, refetch_interval: int,
                 feeds: List[RSSFeed],
                 publisher: Optional[IPublisher],
                 ):
        self.refetch_interval = refetch_interval
        self.publisher = publisher
        self.feeds = feeds

    async def shutdown(self):
        pass

    async def start(self):
        session = aiohttp.ClientSession()
        results = []
        async with session:
            for feed in self.feeds:
                response = await session.get(feed.source_url)
                body = await response.text()
                articles = feed.parser(body).parse()
                results.extend(articles)
        logger.info("Successfully parsed %d articles from %s sources",
                    len(results), len(self.feeds))
