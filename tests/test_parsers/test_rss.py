from parsers import UnianRssParser


class TestUnianParser:
    def test_parses_correctly(self, unian_rss):
        parser = UnianRssParser(unian_rss)
        articles = parser.parse()
        assert len(articles) > 0
