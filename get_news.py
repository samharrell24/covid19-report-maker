from newsapi import NewsApiClient
from dataclasses import dataclass
import datetime as dt


@dataclass(frozen=False)
class site:
    source: str
    author: str
    title: str
    url: str
    date_published: str
    content: str
# , cnn, cnbc, new-york-times, fox-news, the-washington-post

def get_article_data():
    client = NewsApiClient(api_key='32ac179029f9427c8c7a61f40e48c7c7')
    top_headlines = client.get_top_headlines(q='coronavirus',
                                             language='en',
                                             sources='bbc-news, cnn, cnbc, new-york-times, fox-news')

    # top_headlines is a dict that contains ['status', 'totalResults', 'articles']
    print(top_headlines['totalResults'])
    create_pretty_list(top_headlines['articles'], top_headlines['totalResults'])


def create_pretty_list(dict, size):
    aList = []

    for i in range(0, size):
        if i == size-1:
            exit()
        else:
            for key, value in dict[i].items():
                print(f"\n{key.ljust(15)} {value}")


def main():
    get_article_data()


if __name__ == '__main__':
    main()
