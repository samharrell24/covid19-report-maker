from newsapi import NewsApiClient
from dataclasses import dataclass
import datetime as dt


@dataclass(frozen=False)
class site:
    source: str
    author: str
    title: str
    description: str
    url: str
    date_published: str
    content: str


def get_article_data():
    client = NewsApiClient(api_key='32ac179029f9427c8c7a61f40e48c7c7')
    top_headlines = client.get_top_headlines(q='coronavirus',
                                             language='en',
                                             sources='bbc-news, cnn, cnbc, new-york-times, fox-news')

    # top_headlines is a dict that contains ['status', 'totalResults', 'articles']
    aList = create_pretty_list(top_headlines['articles'], top_headlines['totalResults'])
    return aList


def create_pretty_list(dict, size):
    aList = []

    for i in range(0, size):
        temp_site = site("", "", "", "", "", "", "")

        for key, value in dict[i].items():
            if key == "source":
                temp_site.source = value
            elif key == "author":
                temp_site.author = value
            elif key == "title":
                temp_site.title = value
            elif key == "description":
                temp_site.description = value
            elif key == "url":
                temp_site.url = value
            elif key == "publishedAt":
                temp = value.split("T")
                temp2 = temp[1].split("Z")
                temp_site.date_published = temp[0] + " at " + temp2[0]
            elif key == "content":
                temp_site.content = value

        aList.append(temp_site)

    return aList


def main():
    aList = get_article_data()
    for x in aList:
        print(x)


if __name__ == '__main__':
    main()
