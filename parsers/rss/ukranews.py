from io import StringIO
from xml.etree import ElementTree

from .base import BaseRSSParser


class UkraNewsRssParser(BaseRSSParser):
    source = "ukranews"

    @staticmethod
    def _create_root_xml(raw_response: str) -> ElementTree:
        it = ElementTree.iterparse(StringIO(raw_response))
        for _, el in it:
            prefix, has_namespace, postfix = el.tag.partition('}')
            if has_namespace:
                el.tag = postfix  # strip all namespaces
        return it.root

    def _parse_description(self, element: ElementTree.Element) -> str:
        description = element.find(self.attr_mapping["description"])
        if description:
            return description.text
        return ""


if __name__ == '__main__':
    def main():
        with open("../../tests/stubs/stub_ukranews_rss.xml") as f:
            c = f.read()
            p = UkraNewsRssParser(c)
            articles = p.parse()
            print(articles)
    main()
