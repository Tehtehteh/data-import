from .base import BaseRSSParser

from xml.etree import ElementTree


class UnianRssParser(BaseRSSParser):
    source = 'Unian'

    def _parse_image_link(self, element: ElementTree.Element) -> str:
        return element.find("enclosure").get("url")
