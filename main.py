from parsers.rss import (
    BaseRSSParser,
    PravdaRssParser
)

from stub import unian_rss_example
from xml.etree import ElementTree


def parse_pravda():
    pravda_stub = "stub_pravda_rss.xml"
    et = ElementTree.parse(pravda_stub)
    parser = PravdaRssParser(et.getroot())
    articles = parser.parse()
    print(articles)

def main():
    # unian_stub = "stub_unian_rss.xml"
    # et = ElementTree.parse(unian_stub)
    # parser = BaseRSSParser(et.getroot())
    # articles = parser.parse()
    # print(articles)
    parse_pravda()


if __name__ == '__main__':
    main()
