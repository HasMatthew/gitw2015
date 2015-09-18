import argparse
import requests
import logging
from pprint import pprint

HOST = 'http://dh-dane03-dev.sea3.office.priv:8080'
CHALLENGES_PATH = 'challenges'


def end_state(start):
    '''
    end_state returns a solution state given the starting state defined by a dictionary with structure
    [
        {
            "id": "A",
            "edges": [
                4,
                1,
                2,
                3
            ]
        },
        {
            "id": "B",
            "edges": [
                7,
                2,
                5,
                6
            ]
        }
    ],
    [
        {
            "id": "C",
            "edges": [
                3,
                8,
                9,
                10
            ]
        },
        {
            "id": "D",
            "edges": [
                11,
                12,
                8,
                7
            ]
        }
    ]
    '''
    pass


def moves(start, end):
    '''
    start and end are dictionaries that define the beginning and end puzzle state with structure
    [
        {
            "id": "A",
            "edges": [
                4,
                1,
                2,
                3
            ]
        },
        {
            "id": "B",
            "edges": [
                7,
                2,
                5,
                6
            ]
        }
    ],
    [
        {
            "id": "C",
            "edges": [
                3,
                8,
                9,
                10
            ]
        },
        {
            "id": "D",
            "edges": [
                11,
                12,
                8,
                7
            ]
        }
    ]
    and returns a list of moves to transition from beginning to end
    '''
    pass


def get_board(id):
    url = HOST + '/' + CHALLENGES_PATH + '/' + id
    r = requests.get(url)
    return r.json()['board']


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(message)s')

    parser = argparse.ArgumentParser(
        description='Solves 15-challenge style puzzles',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--id', required=True, help='the puzzle ID to fetch and solve')
    args = parser.parse_args()
    pprint(vars(args))

    pprint(get_board(args.id))


if __name__ == "__main__":
    main()
