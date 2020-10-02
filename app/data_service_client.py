import aiohttp
import logging
import json

from parsers import RSSFeed
from .implemented_sources import ImplementedSources

from typing import List


class DataServiceClient:

    def __init__(self, debug: bool = False):
        self.debug = debug

    async def get_sources(self, url: str) -> List[RSSFeed]:
        if self.debug:
            with open('tests/stubs/stub_data_client_sources.json') as handle:
                response = json.load(handle)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as request:
                    response = await request.json()

        result = list()
        for obj in response:
            source = ImplementedSources.get_source(obj['name'])
            if source:
                result.append(RSSFeed(obj['url'], source))
            else:
                logging.warning(f"Source {obj['name']} does not exist")

        return result
