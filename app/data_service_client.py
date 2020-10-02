from parsers import (
    UnianRssParser,
    PravdaRssParser,
    UkraNewsRssParser,
    LigaRssParser
)
from typing import List, Tuple


class DataServiceClient:
    parsers = {
        "unian": UnianRssParser,
        "pravda": PravdaRssParser,
        "ukranews": UkraNewsRssParser,
        "liga": LigaRssParser
    }

    @staticmethod
    def get_sources() -> List[Tuple[str, any]]:
        response = [
            {
                "type": "rss",
                "name": "pravda",
                "url": "https://www.pravda.com.ua/rus/rss/"
            },
            {
                "type": "rss",
                "name": "liga",
                "url": "https://www.liga.net/news/all/rss.xml"
            },
            {
                "type": "rss",
                "name": "unian",
                "url": "https://rss.unian.net/site/news_ukr.rss"
            },
            {
                "type": "rss",
                "name": "ukranews",
                "url": "https://ukranews.com/rss-gen/Sub=2&Sub=3&Sub=4&Sub=5&Sub=6&Sub=7&Sub=8&Sub=9&Sub=10&Sub=599&Sub=610&Sub=611&Sub=612&Sub=614&Sub=615&Sub=616&Sub=617&Sub=618&Sub=619&Sub=620&Sub=621&Sub=622&Sub=623&Sub=624&Sub=625&Sub=626&Sub=627&Sub=628&Sub=629&Sub=630&Sub=631&Sub=632&Sub=633&Sub=718&Sub=719&Sub=720&Sub=721&Sub=722&Sub=723&Sub=724&Sub=725&Sub=726&Reg=4&Reg=5&Reg=8&Reg=9&Reg=10&Reg=12&Reg=13&Reg=14&Reg=15&Reg=17&Reg=18&Reg=19&Reg=20&Reg=21&Reg=22&Reg=23&Reg=24&Reg=25&Reg=26&Reg=27&Reg=28&Reg=29&Reg=30&Reg=31&Reg=32"
            },

        ]
        response = [(obj['url'], DataServiceClient.parsers[obj['name']]) for obj in response]
        return response
