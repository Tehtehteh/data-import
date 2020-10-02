import aiohttp
import logging
import json

from parsers import RSSFeed
from .implemented_sources import ImplementedSources

from typing import List


class DataServiceClient:
    """
    It is a client for "Data Service",
    which returns a list of objects with info to connect to different RSS sources.
    """

    def __init__(self, base_url: str, debug: bool = False):
        self.debug = debug
        self.base_url = base_url

    async def get_rss_sources(self, url: str) -> List[RSSFeed]:
        if self.debug:
            with open('tests/stubs/stub_data_client_sources.json') as handle:
                response = json.load(handle)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base_url + url) as request:
                    response = await request.json()

        result = list()
        for obj in response:
            source = ImplementedSources.get_source(obj['name'])
            if source:
                result.append(RSSFeed(obj['url'], source))
            else:
                logging.warning(f"Source {obj['name']} does not exist")

        return result
