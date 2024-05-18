import argparse
from ankivocab.vocab_card import VocabCard
import csv

def add_vocab_card(word, gender, info, context, definition, pictures, pronunciation, recording, test_spelling):
    pictures_list = pictures.split(",") if pictures else []
    card = VocabCard(word, gender, info, context, definition, pictures_list, pronunciation, recording, test_spelling)
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
    parser.add_argument('--export', metavar='FILENAME', help="Export vocabulary cards to a CSV file")

    args = parser.parse_args()

    cards = []

    if args.add:
        word, gender, info, context, definition, pictures, pronunciation, recording, test_spelling = args.add
        card = add_vocab_card(word, gender, info, context, definition, pictures, pronunciation, recording, test_spelling)
        cards.append(card)
        print(f"Added: {card}")

    if args.export:
        export_to_csv(cards, args.export)
        print(f"Exported to {args.export}")

if __name__ == "__main__":
    main()
