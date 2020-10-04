from xml.etree import ElementTree

from .base import BaseRSSParser


class LigaRssParser(BaseRSSParser):
    source = "liga"

    def _parse_image_link(self, element: ElementTree.Element) -> str:
        return element.find("enclosure").get("url")
