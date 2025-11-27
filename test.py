# https://github.com/opsdisk/yagooglesearch

from duckduckgo_search import DDGS
from googlesearch import search


def ddg_search(query):    
    if query == "":
        query = "Python programming tutorial"

    # Initialize the DDGS class
    ddgs = DDGS()

    # Perform a text search
    search_results = ddgs.text(keywords=query, max_results=3, region='us-en')
    #search_results = ddgs.news(keywords=query, max_results=5, region='us-en')

    # Iterate and print the results
    print(f"Search results for '{query}':")
    for r in search_results:
        print(f"Title: {r['title']}")
        print(f"Link: {r['href']}")
        print(f"Snippet: {r['body']}")
        print("-" * 20)


def test_google_search(query):

    if query == "":
        query = "Python programming tutorial"

    # Perform the search
    # tld: top-level domain to use (e.g., "co.in" for India)
    # num: number of results per page
    # stop: total number of results to retrieve
    # pause: delay between requests to avoid being blocked
    #search_results = search(query, tld="com", num=10, stop=5, pause=2)

    search_results = search(query)

    # Print the URLs from the search results
    print(type(search_results))
    print(f"Search results for '{query}':")

    print(list(search_results))

    print("original results")
    for url in search_results:
        print(url)


#test_google_search("divide by zero error in python")

ddg_search("fix the bug in the google search code")

#ddg_search("divide by zero error in python")


