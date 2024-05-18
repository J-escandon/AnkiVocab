# src/ankivocab/cli.py

import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
from ankivocab.vocab_card import VocabCard
from ankivocab.web_scraper import WebScraper
import csv

def add_vocab_card_auto(word):
    scraper = WebScraper(word)
    definition = scraper.fetch_definition()

    card = VocabCard(word, definition=definition)
    return card

def export_to_csv(cards, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Gender", "Info", "Context", "Definition", "Picture", "Pronunciation (Recording and/or IPA)", "Recording", "Test Spelling? (y = yes, blank = no)"])
        for card in cards:
            writer.writerow(card.to_csv_row())

def main():
    parser = argparse.ArgumentParser(description="AnkiVocab CLI tool")
    parser.add_argument('--add', nargs=9, metavar=('WORD', 'GENDER', 'INFO', 'CONTEXT', 'DEFINITION', 'PICTURE', 'PRONUNCIATION', 'RECORDING', 'TEST_SPELLING'),
                        help="Add a new vocabulary card")
    parser.add_argument('--add-auto', nargs='+', metavar='WORD', help="Add new vocabulary cards with auto-filled fields")
    parser.add_argument('--export', metavar='FILENAME', help="Export vocabulary cards to a CSV file")

    args = parser.parse_args()

    cards = []

    if args.add:
        word, gender, info, context, definition, pictures, pronunciation, recording, test_spelling = args.add
        card = VocabCard(word, gender, info, context, definition, pictures, pronunciation, recording, test_spelling)
        cards.append(card)
        print(f"Added: {card}")

    if args.add_auto:
        for word in args.add_auto:
            card = add_vocab_card_auto(word)
            cards.append(card)
            print(f"Added: {card}")

    if args.export:
        export_to_csv(cards, args.export)
        print(f"Exported to {args.export}")

if __name__ == "__main__":
    main()
