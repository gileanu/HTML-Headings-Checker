import sys
import requests
from bs4 import BeautifulSoup

def scrape_headings(url: str, include_paragraphs: bool = False, include_links: bool = False):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    total_headings = 0
    headings_by_level = {}

    for level in range(1, 7):  # h1 through h6
        headings = soup.find_all(f"h{level}")
        if headings:
            headings_by_level[level] = headings
            total_headings += len(headings)

    print(f"\nHeadings found on {url}:\n" + "-"*40)
    print(f"\nTotal headings found: {total_headings}\n")

    for level, headings in headings_by_level.items():
        print(f"{len(headings)} h{level} headings found:")
        for i, heading in enumerate(headings, start=1):
            text = heading.get_text(strip=True)
            print(f"<h{level}> #{i}: {text}")
        print()

    if include_paragraphs:
        paragraphs = soup.find_all("p")
        print(f"\n{len(paragraphs)} <p> tags found:\n")
        for i, p in enumerate(paragraphs, start=1):
            text = p.get_text(strip=True)
            if text:
                print(f"<p> #{i}: {text}")
        print()

    if include_links:
        links = soup.find_all("a")
        print(f"\n{len(links)} <a> tags found:\n")
        for i, a in enumerate(links, start=1):
            text = a.get_text(strip=True)
            href = a.get("href", "")
            if text or href:
                print(f"<a> #{i}: text='{text}' | href='{href}'")
        print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scrape_headings.py <website_url> [--include-paragraphs|-p] [--include-links|-a]")
        sys.exit(1)
    
    url = sys.argv[1].strip()
    include_paragraphs = "--include-paragraphs" in sys.argv or "-p" in sys.argv
    include_links = "--include-links" in sys.argv or "-a" in sys.argv
    scrape_headings(url, include_paragraphs, include_links)