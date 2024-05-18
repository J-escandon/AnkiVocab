# src/ankivocab/web_scraper.py

import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, word):
        self.word = word

    def fetch_definition(self):
        url = f"https://www.vandale.nl/gratis-woordenboek/nederlands/betekenis/{self.word}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            definitions = []
            definition_elements = soup.select('span.f3.f0g')
            for element in definition_elements:
                definition_number = element.select_one('span.fz > span.f4').text.strip()
                definition_parts = [span.text.strip() for span in element.select('span.f0 > span.fr')]
                definition_text = " ".join(definition_parts)
                definitions.append(f"{definition_number}. {definition_text}")

            if definitions:
                return "\n".join(definitions)
            else:
                return None
        else:
            return None

if __name__ == "__main__":
    word = "wanhopig"
    scraper = WebScraper(word)
    print(f"Definition of {word}: {scraper.fetch_definition()}")
