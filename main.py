from parsers.rss import (
    PravdaRssParser,
    UnianRssParser
)


def parse_pravda():
    pravda_stub = "stub_pravda_rss.xml"
    with open(pravda_stub) as fh:
        stub = fh.read()
        parser = PravdaRssParser(stub)
        articles = parser.parse()
        return articles


def parse_unian():
    unian_stub = "stub_unian_rss.xml"
    with open(unian_stub) as fh:
        stub = fh.read()
        parser = UnianRssParser(stub)
        articles = parser.parse()
        return articles


def main():
    articles = []
    pravda = parse_pravda()
    unian = parse_unian()
    articles.extend(pravda)
    articles.extend(unian)
    import random
    random.shuffle(articles)
    print(articles)


if __name__ == '__main__':
    main()
