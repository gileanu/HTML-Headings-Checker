import sys
import requests
from bs4 import BeautifulSoup

def scrape_headings(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    print(f"\nHeadings found on {url}:\n" + "-"*40)
    
    for level in range(1, 7):  # h1 through h6
        headings = soup.find_all(f"h{level}")
        if headings:
            print(f"\n{len(headings)} h{level} headings found:")
            for i, heading in enumerate(headings, start=1):
                text = heading.get_text(strip=True)
                print(f"<h{level}> #{i}: {text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scrape_headings.py <website_url>")
        sys.exit(1)
    
    url = sys.argv[1].strip()
    scrape_headings(url)