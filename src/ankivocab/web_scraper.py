import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, word):
        self.word = word

    def fetch_definition(self):
        # Example of fetching a definition from a website
        url = f"https://example-dictionary.com/word/{self.word}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            definition = soup.find('div', class_='definition').text.strip()
            return definition
        return None

    # Add methods for fetching other fields similarly

if __name__ == "__main__":
    word = "example"
    scraper = WebScraper(word)
    print(f"Definition of {word}: {scraper.fetch_definition()}")
