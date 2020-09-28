from xml.etree import ElementTree
from io import StringIO

from .base import BaseRSSParser


class PravdaRssParser(BaseRSSParser):

    source = 'Pravda'

    @staticmethod
    def _create_root_xml(raw_response: str) -> ElementTree:
        it = ElementTree.iterparse(StringIO(raw_response))
        for _, el in it:
            prefix, has_namespace, postfix = el.tag.partition('}')
            if has_namespace:
                el.tag = postfix  # strip all namespaces
        return it.root

    # def _parse_image_link(self, element: ElementTree.Element) -> str:
    #     return element.find("enclosure").get("url")

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
