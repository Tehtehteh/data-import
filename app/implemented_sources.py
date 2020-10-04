import logging

from typing import List, Dict

from parsers.rss import (
    RSSFeed,
    LigaRssParser,
    PravdaRssParser,
    UkraNewsRssParser,
    UnianRssParser,
)


class ImplementedSources:
    """
    maps source`s name to class which implements it`s RSS parser
    """

    sources = {
        'liga': LigaRssParser,
        'pravda': PravdaRssParser,
        'ukranews': UkraNewsRssParser,
        'unian': UnianRssParser
    }

    @staticmethod
    def get_implemented_sources_map(data_client_response: List[Dict[str, any]]) -> List[RSSFeed]:
        """
        returns a list of RSSFeed instances for each implemented source in a list
        """
        res = []
        for obj in data_client_response:
            source = ImplementedSources.sources.get(obj['name'])
            if source:  # skip all not implemented sources
                res.append(RSSFeed(obj['url'], source))
            else:
                logging.warning(f"Source {obj['name']} does not exist")
        return res
