# HTML-Headings-Checker

Python script that scrapes and organizes HTML content from a given website URL. By default, it extracts all heading tags (h1 through h6), grouping them by level and showing both counts and text.

## It also supports optional flags:

--include-paragraphs (-p) = lists all paragraph tags with their text.<br>
--include-links (-a) = lists all anchor tags with their visible text and href attribute.

The script displays an overall heading count, per-level counts, and neatly formatted results. It handles errors gracefully (e.g., connection issues) and lets users combine flags (-p -a) to extract multiple tag types at once.

## Libraries used:

sys<br>
BeautifulSoup4<br>
requests

## Usage

python check.py https://example.com<br>
python check.py https://example.com -p<br>
python check.py https://example.com -a<br>
python check.py https://example.com -p -a
