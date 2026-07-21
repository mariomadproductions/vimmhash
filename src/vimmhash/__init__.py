from vimmhash import util
import argparse
import requests
import itertools

BASE_URL = 'https://vimm.net/vault/?p=list&q='

def get_args():
    parser = argparse.ArgumentParser(prog='vimmhash')
    parser.add_argument('FILES', nargs='+')
    return parser.parse_args()

def main():
    args = get_args()
    
    with requests.Session() as session:
        session.headers.update({'Accept': 'application/json'})
        for path in args.FILES:
            with util.open(path, 'rt', encoding='utf8') as f:
                lines_strp = (line.strip() for line in f)
                for batch in itertools.batched(lines_strp, 100):
                    search_string = ','.join(batch)
                    url = f'{BASE_URL}{search_string}'
                    response = session.get(url)
                    json = response.json()
                    for game in json['games']:
                        print(game['url'])
