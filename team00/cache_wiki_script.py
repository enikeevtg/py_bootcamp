import argparse
import requests
import webbrowser
import os
from bs4 import BeautifulSoup


FILE_FOR_CHECKS = "./pages.txt"
RESOURCE = "https://wikipedia.org/wiki/"

parser = argparse.ArgumentParser(prog="cache_wiki.py",
                                description="download pages from Wikipedia")
parser.add_argument('-p', '--page', type=str, default='Erdős number')
parser.add_argument('-d', '--depth', type=int, default=3)
article = parser.parse_args().page.split()
article_url = RESOURCE + "_".join(article)
print(article_url)

page = requests.get(article_url)
soup = BeautifulSoup(page.content, "html.parser")

# with for loop:
with open(FILE_FOR_CHECKS, 'w') as fp:
    for a_tag in soup.find("div", id="bodyContent").find_all("a"):
        if a_tag.get("href")[:6] == "/wiki/":
            fp.writelines(RESOURCE + a_tag.get("href")[6:] + "\n")

# # with generator expression:
# links = (x.get("href") for x in soup.find_all("a")
# if x.get("href")[:6] == "/wiki/")

# with open(FILE_FOR_CHECKS, 'w') as fp:
#     for link in links:
#         fp.writelines(link)
#         fp.writelines('\n')



