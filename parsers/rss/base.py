import logging

from typing import List, Optional
from parsers.types import Article
from xml.etree import ElementTree


class BaseRSSParser:

    logger = logging.getLogger(__name__)
    DEFAULT_ARTICLES_ATTR_MAPPING = {
        "id": "guid",
        "link": "link",
        "title": "title",
        "description": "description",
        "image": "image",
        "image_description": "description"
    }

    def __init__(self, raw_response: str,
                 rss_version: str = "2.0",
                 articles_attr_mapping: Optional[dict] = None):
        self.rss_version = rss_version
        self.rss_tree = ElementTree.fromstring(self.pre_parse(raw_response))
        self.attr_mapping = articles_attr_mapping

    def pre_parse(self, raw_response: str):
        return raw_response

    @property
    def attr_mapping(self):
        return self._attr_mapping

    @attr_mapping.setter
    def attr_mapping(self, value: Optional[dict] = None):
        if value:
            self._attr_mapping = self.DEFAULT_ARTICLES_ATTR_MAPPING.update(value)
        self._attr_mapping = self.DEFAULT_ARTICLES_ATTR_MAPPING

    def get_article_iterator(self):
        return self.rss_tree.find("channel").findall("item")

    def parse(self) -> List[Article]:
        articles: List[Article] = []
        for child in self.get_article_iterator():
            id_ = self._parse_id(child)
            link = self._parse_link(child)
            title = self._parse_title(child)
            title = self._normalize_text(title)
            description = self._parse_description(child)
            description = self._normalize_text(description)
            image_link = self._parse_image_link(child)
            image_description = self._parse_image_description(child)
            article = Article(id_, link, title, description,
                              image_link, image_description)
            articles.append(article)
        return articles

    def _parse_link(self, element: ElementTree.Element) -> str:
        return element.find(self.attr_mapping["link"]).text

    def _parse_id(self, element: ElementTree.Element) -> str:
        return element.find(self.attr_mapping["id"]).text

    def _parse_title(self, element: ElementTree.Element) -> str:
        return element.find(self.attr_mapping["title"]).text

    def _parse_description(self, element: ElementTree.Element) -> str:
        return element.find(self.attr_mapping["description"]).text

    def _parse_image_link(self, element: ElementTree.Element) -> str:
        image_element = element.find(self.attr_mapping["image"])
        if image_element:
            return image_element.find("link").text
        return ""

    def _parse_image_description(self, element: ElementTree.Element) -> str:
        image_element = element.find(self.attr_mapping["image"])
        if image_element:
            return image_element.find(self.attr_mapping["image_description"]).text
        return ""

    @staticmethod
    def _normalize_text(raw_text: str) -> str:
        return raw_text.lstrip("\n").rstrip("\n").strip()
