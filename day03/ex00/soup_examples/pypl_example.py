from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>good<i>HTML<i>qwertfd", features="lxml")
print(soup.prettify())

print(soup.find(string="good"))
print(soup.i)
