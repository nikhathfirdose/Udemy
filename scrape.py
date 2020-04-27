import requests  # allows to download html
from bs4 import BeautifulSoup  # allows us to scrape the file
import pprint

pageno = 3
# gives the html respone of this url
res = requests.get(f"https://news.ycombinator.com/news?p={pageno}")
# using soup to parse the respone in htl format
soup = BeautifulSoup(res.text, "html.parser")
allLinks = soup.select(".storylink")
allSubVotes = soup.select(".subtext")


def sortingVotes(resultDict):
    return sorted(resultDict, key=lambda k: k["votes"], reverse=True)


def linksData(l, s):
    links = []
    count = 0
    for idx, item in enumerate(l):  # to get a index value we use enumerate
        title = item.getText()
        # None for just in case there was no href present ie, t acts as a default value holder
        href = item.get("href", None)  # this item is saame as l[idx]
        vote = s[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", " "))
            if(points > 55):
                [points].sort()
                links.append({"title": title, "link": href, "votes": points})
                count += 1
    return sortingVotes(links), count


pprint.pprint(linksData(allLinks, allSubVotes))
