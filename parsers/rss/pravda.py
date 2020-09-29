from xml.etree import ElementTree
from io import StringIO

from .base import BaseRSSParser


class PravdaRssParser(BaseRSSParser):

    source = 'Pravda'

    def _parse_title(self, element: ElementTree.Element) -> str:
        # todo: don't call normalize text multiple times
        title = super()._parse_title(element)
        if self._normalize_text(title):
            return title
        return f'{list(element.find("title"))[0].text} {list(element.find("title"))[0].tail}'

    def _parse_description(self, element: ElementTree.Element) -> str:
        return element.find("description").text or ""

    def get_article_iterator(self):
        return self.rss_tree.findall(".//item")
