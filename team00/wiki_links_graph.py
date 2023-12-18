import requests
from bs4 import BeautifulSoup
import logging
import json
import inspect


class WikiLinksGraph:
    """Wikipedia links-graph producer"""

    __resourse = "https://wikipedia.org"
    __link_flag = "/wiki/"

    def __init__(self, root_page: str, depth: int = 3, pages_limit: int = 1000,
                 dump_to_json: bool = True):
        self.__root_page = root_page
        self.__depth = depth
        self.__pages_limit = pages_limit
        self.__dump_to_json = dump_to_json
        self.__pages_counter = 0

    @staticmethod
    def __get_object_name(self) -> str:
        """get object name for output filename"""

        parent_frame = inspect.currentframe()
        while True:
            for key, value in parent_frame.f_locals.items():
                if key != "self" and value is self:
                    return key
            parent_frame = parent_frame.f_back

    def __create_json_file(self, graph_data, ):
        """JSON-file with graph content creating"""

        filename = self.__get_object_name(self) + "_links_graph.json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(graph_data, file, sort_keys=False, indent=2,
                      ensure_ascii=False)

    def __get_page(sell, url: str) -> requests.Response:
        page = requests.get(url)
        if page.status_code == 200:
            return page

    def __make_graph(self, url: str) -> dict:
        pass

    def get_graph(self) -> dict:
        page = self.__get_page(self.__root_page)
        print(page)


wiki = WikiLinksGraph("https://wikipedia.org/qwerthgfd")
wiki.get_graph()
