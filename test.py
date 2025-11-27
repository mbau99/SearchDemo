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


# only this code works: (it was initially done in colab, based on suggestion from Gemini)
import requests

def simple_web_search_api(query, api_key, cx_id, num_results=5):
    """
    Performs a simple web search using the Google Custom Search JSON API.

    Args:
        query (str): The search query.
        api_key (str): Your Google API Key with Custom Search API enabled.
        cx_id (str): Your Custom Search Engine ID (CX).
        num_results (int): The number of search results to retrieve (max 10 per request).

    Returns:
        list: A list of dictionaries, each representing a search result (title, link, snippet).
              Returns an empty list if an error occurs or no results are found.
    """
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx_id,
        "q": query,
        "num": min(num_results, 10) # Max 10 results per request for this API
    }

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()

        results = []
        if 'items' in data:
            for item in data['items']:
                results.append({
                    'title': item.get('title'),
                    'link': item.get('link'),
                    'snippet': item.get('snippet')
                })
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return []
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return []

# --- Example Usage --- START
# IMPORTANT: Replace these with your actual API Key and Custom Search Engine ID
# You can store these securely using `from google.colab import userdata`
# For example:
# GOOGLE_API_KEY = userdata.get('YOUR_GOOGLE_API_KEY_NAME')
# CUSTOM_SEARCH_ENGINE_ID = userdata.get('YOUR_CUSTOM_SEARCH_ENGINE_ID_NAME')

YOUR_GOOGLE_API_KEY = "AIzaSyDbmAkXL0n5OL8aGgSWp6Bgl-eCjlNQlrY" # <-- REPLACE THIS
YOUR_CUSTOM_SEARCH_ENGINE_ID = "1575da05955d24f76" # <-- REPLACE THIS  278c1a819e8bb4fea

if YOUR_GOOGLE_API_KEY == "YOUR_API_KEY_HERE" or YOUR_CUSTOM_SEARCH_ENGINE_ID == "YOUR_CX_ID_HERE":
    print("Please update 'YOUR_GOOGLE_API_KEY' and 'YOUR_CUSTOM_SEARCH_ENGINE_ID' with your actual credentials.")
else:
    search_query = "Can you figure out why the there is a bug in the Agent code?"
    search_results = simple_web_search_api(search_query, YOUR_GOOGLE_API_KEY, YOUR_CUSTOM_SEARCH_ENGINE_ID, num_results=3)

    if search_results:
        print(f"\nSearch results for '{search_query}':")
        for i, result in enumerate(search_results):
            print(f"\n{i+1}. Title: {result['title']}")
            print(f"   Link: {result['link']}")
            print(f"   Snippet: {result['snippet']}")
    else:
        print("No search results found or an error occurred.")
# --- Example Usage --- END


#test_google_search("divide by zero error in python")
#ddg_search("fix the bug in the google search code")



