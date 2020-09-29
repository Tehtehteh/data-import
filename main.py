import signal
import asyncio
import logging

from config import Config
from app import Application
from logs import setup_logging
from parsers import (
    UnianRssParser,
    PravdaRssParser,
    UkraNewsRssParser,
    RSSFeed, LigaRssParser,
)


logger = logging.getLogger('main')


async def shutdown(app: Application) -> None:
    logger.info('Shutting down application...')
    await app.shutdown()
    logger.info('Done shutting down application.')
    logging.shutdown()


def make_app() -> Application:
    config = Config()
    pravda_feed = RSSFeed("https://www.pravda.com.ua/rus/rss/",
                          PravdaRssParser)
    unian_feed = RSSFeed("https://rss.unian.net/site/news_ukr.rss",
                         UnianRssParser)
    ukranews_feed = RSSFeed("https://ukranews.com/rss-gen/Sub=2&Sub=3&Sub=4&Sub=5&Sub=6&Sub=7&Sub=8&Sub=9&Sub=10&Sub=599&Sub=610&Sub=611&Sub=612&Sub=614&Sub=615&Sub=616&Sub=617&Sub=618&Sub=619&Sub=620&Sub=621&Sub=622&Sub=623&Sub=624&Sub=625&Sub=626&Sub=627&Sub=628&Sub=629&Sub=630&Sub=631&Sub=632&Sub=633&Sub=718&Sub=719&Sub=720&Sub=721&Sub=722&Sub=723&Sub=724&Sub=725&Sub=726&Reg=4&Reg=5&Reg=8&Reg=9&Reg=10&Reg=12&Reg=13&Reg=14&Reg=15&Reg=17&Reg=18&Reg=19&Reg=20&Reg=21&Reg=22&Reg=23&Reg=24&Reg=25&Reg=26&Reg=27&Reg=28&Reg=29&Reg=30&Reg=31&Reg=32",
                            UkraNewsRssParser)
    liga_feed = RSSFeed(
        "https://www.liga.net/news/all/rss.xml",
        LigaRssParser)
    app = Application(refetch_interval=config.refetch_time,
                      feeds=[pravda_feed, unian_feed, ukranews_feed, liga_feed], publisher=None)
    return app


async def main() -> None:
    loop = asyncio.get_running_loop()
    setup_logging()
    app = make_app()

    logger.info('Running app...Refetch interval interval: %s.',
                app.refetch_interval)
    for signum in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(signum,
                                lambda: asyncio.ensure_future(shutdown(app)))
    await app.start()


if __name__ == '__main__':
    # def main():
    #     with open("tests/stubs/stub_liga_rss.xml") as f:
    #         c = f.read()
    #         p = LigaRssParser(c)
    #         articles = p.parse()
    #         print(articles)
    # main()

    asyncio.run(main())
