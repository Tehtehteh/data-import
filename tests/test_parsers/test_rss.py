from parsers import (
    UnianRssParser,
    PravdaRssParser,
    UkraNewsRssParser
)


class TestUnianParser:
    def test_parses_correctly(self, unian_rss):
        parser = UnianRssParser(unian_rss)
        articles = parser.parse()
        assert len(articles) > 0


class TestPravdaParser:
    def test_parses_correctly(self, pravda_rss):
        parser = PravdaRssParser(pravda_rss)
        articles = parser.parse()
        assert len(articles) > 0


class TestUkraNewsParser:
    def test_parses_correctly(self, ukranews_rss):
        parser = UkraNewsRssParser(ukranews_rss)
        articles = parser.parse()
        assert len(articles) > 0
