import signal
import asyncio
import logging

from config import Config
from app import Application, DataServiceClient
from logs import setup_logging
from parsers import RSSFeed


logger = logging.getLogger('main')


async def shutdown(app: Application) -> None:
    logger.info('Shutting down application...')
    await app.shutdown()
    logger.info('Done shutting down application.')
    logging.shutdown()


def make_app() -> Application:
    config = Config()
    feeds = [RSSFeed(*feed) for feed in DataServiceClient.get_sources()]
    app = Application(refetch_interval=config.refetch_time, feeds=feeds, publisher=None)
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
