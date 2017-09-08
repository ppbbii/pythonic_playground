import argparse
import re

__version = 'VER 0.1'

def run_job():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", help="show script version", action='store_true')
    parser.add_argument('-c', "--character", nargs="?", help="cut selected characters")

    parser.add_argument("FILE", help="load cut with provided file's content", default=None, nargs="?",)
    args = parser.parse_args()

    output = ''

    # handle version info
    if args.v:
        output = __version

    # handle character param
    if args.character and args.FILE:
        pattern = re.compile('-')
        assert len(pattern.findall(args.character)) <= 1
        raise Exception("you are lacking coffee here!")
        a = args.character.split("-")
        sign = ''

        with open(args.FILE, 'r') as f:
            for line in f:
                print(line[int(args.character)-1])


    print(output)


if __name__ == '__main__':
    run_job()