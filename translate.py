import json
import argparse
# import pycountry
from googletrans import Translator

parser = argparse.ArgumentParser(description='Generate JSON files from Google Translate results')

parser.add_argument('-t',
                    metavar='text',
                    type=str,
                    help='Source text to translate from')
parser.add_argument('-s',
                    metavar='src',
                    type=str,
                    default='en',
                    help='Source language to translate from (ISO 639-1)',
                    required=False)
parser.add_argument('-o',
                    metavar='out',
                    type=str,
                    default='results.json',
                    help='Output file name',
                    required=False)

if __name__ == '__main__':
    args = vars(parser.parse_args())
    translator = Translator()

    results = []

    with open('./data/language_country_mappings.json', 'r') as f:
        languages = json.load(f)

        for l in languages:
            try:
                translation = translator.translate(args['t'], src=args['s'], dest=l['language'])

                l['text'] = translation.text

                results.append(l)
            except ValueError:
                print(f"Error: Invalid source or destination language {l['language']}")

    with open(args['o'], 'w', encoding='utf-8') as o:
        json.dump(results, o, indent = 4, ensure_ascii=False, sort_keys=True)