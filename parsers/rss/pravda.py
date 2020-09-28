from xml.etree import ElementTree

from .base import BaseRSSParser


class PravdaRssParser(BaseRSSParser):

    # def pre_parse(self,):

    def _parse_image_link(self, element: ElementTree.Element) -> str:
        return element.find("enclosure").get("url")

    def get_article_iterator(self):
        return self.rss_tree.find(".//channel").findall(".//item")
