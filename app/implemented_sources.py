import importlib

from typing import List, Dict, Union

from parsers.rss import BaseRSSParser


class ImplementedSources:

    @staticmethod
    def get_implemented_sources_map(names: List[str]) -> Dict[str, BaseRSSParser]:
        res = dict()
        for name in names:
            res[name] = ImplementedSources.get_source(name)
        return dict()

    @staticmethod
    def get_source(name: str) -> Union[BaseRSSParser, None]:
        try:
            rss_parser = getattr(importlib.import_module(f"parsers.rss.{name}"), name)
        except ModuleNotFoundError:
            return None
        else:
            return rss_parser
