import argparse
import requests
from bs4 import BeautifulSoup
import logging
import json


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")
OUTPUT_FILE = "./pages.json"
RESOURCE = "https://wikipedia.org"
LINK_FLAG = "/wiki/"
DEFAULT_PAGE = "Erdős number"
DEFAULT_DEPTH = 3


def main():
    article_url, max_depth = get_args()
    wiki_graph = get_links_graph(article_url, max_depth)
    wiki_page_graph = {article_url: wiki_graph}
    write_json(wiki_page_graph)


if __name__ == "__main__":
    main()


def get_args():
    parser = argparse.ArgumentParser(prog="cache_wiki.py",
                                    description="Wikipedia pages graph generator")
    parser.add_argument('-p', '--page', type=str, default=DEFAULT_PAGE)
    parser.add_argument('-d', '--depth', type=int, default=DEFAULT_DEPTH)
    article_url = RESOURCE + LINK_FLAG + \
                  parser.parse_args().page.replace(" ", "_")
    # article = parser.parse_args().page.split()
    # article_url = RESOURCE + "_".join(article)
    max_depth = parser.parse_args().depth
    return (article_url, max_depth)


def get_links_graph(page_url: str, depth: int) -> dict:
    if depth < 0:
        return {}

    links_dict = {page_url: {}}
    for page, links in links_dict.items():
        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, "html.parser")
        links_dict[page_url] = get_links(soup, depth)
        i = 0
        for page, link in links_dict[page_url].items():
            links_dict[page_url][page] = get_links_graph(page, depth - 1)
            i+=1

    return links_dict[page_url]


def get_links(soup: BeautifulSoup, depth: int) -> dict:
    links_dict = {}
    counter = 10
    for a_tag in soup.find("div", id="bodyContent").find_all("a", href=True):
        if counter == 0:
            break
        if (a_tag.get("href")[:6] == LINK_FLAG and
        a_tag.get("href").find(":") == -1):
            # print(a_tag.get("href")[6:])
            link = RESOURCE + a_tag.get("href")
            links_dict[link] = {}
            logging.info(f"depth: {depth}, URL: {link}")
            counter -= 1
    return links_dict


def write_json(graph: dict) -> None:
    with open(OUTPUT_FILE, 'w', encoding='utf8') as fp:
        json.dump(graph, fp, sort_keys=False, indent=2, 
                  ensure_ascii=False)
