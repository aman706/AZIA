from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            top_result = next(results)
            title = top_result["title"]
            url = top_result["href"]
            snippet = top_result["body"]

            # Fetch and summarize the content
            try:
                response = requests.get(url, timeout=5)
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraphs = soup.find_all('p')
                page_text = ' '.join([p.text for p in paragraphs[:3]])
                return f"{title}\n{snippet}\n{page_text[:300]}..."
            except:
                return f"{title}\n{snippet}\n(Content could not be loaded)"
    except:
        return "I couldn’t find anything useful online."

