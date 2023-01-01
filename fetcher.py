import requests
import os
import shutil
import argparse
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

def make_folder(day: int, example: str, inp: str):
    if not os.path.isdir(f'./{day}'):
        os.makedirs(f'./{day}')

    with open(f'./{day}/input.txt', 'w') as inp_file:
        inp_file.write(inp)
    with open(f'./{day}/ex.txt', 'w') as ex_file:
        ex_file.write(example)

    if not os.path.isfile(f'./{day}/{day}.py'):
        shutil.copy('template.py', f'./{day}/{day}.py')

    print(f"input and example files fetched. Template is ready, Happy coding!")


def get_data(day_list: List, headers: Dict):
    for day in day_list:
        inp_resp = requests.get(f'https://adventofcode.com/2022/day/{day}/input', headers = headers)
        ex_resp = requests.get(f'https://adventofcode.com/2022/day/{day}', headers = headers)

        input_data = inp_resp.text.strip()
        example_data = ex_resp.text.split('<pre><code>')[1].split('</code></pre>')[0]

        make_folder(day, example_data, input_data)

def init():
    parser = argparse.ArgumentParser(
            prog = "AOC'22 fetcher",
            description="Fetches the input for given day to input.txt for it's dir",
            )
    parser.add_argument('day', type = int, nargs = '+', help = 'day or days to fetch for')
    args = parser.parse_args()
    day_list = args.day

    AOC_COOKIE = str(os.environ.get("SESSION"))
    if AOC_COOKIE is None:
        print("Check https://github.com/wimglenn/advent-of-code-wim/issues/1 for instructions to get the cookie value, \n Then create a .env file with SESSION=<your_cookie_value>")
        exit()
    headers = {'cookie':'session='+AOC_COOKIE}
    return day_list, headers

if __name__=="__main__":

    day_list, headers = init()
    
    get_data(day_list, headers)


