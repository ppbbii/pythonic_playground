import argparse
import os
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
        # raise Exception("you are lacking coffee here!")
        starting = None
        ending = None

        if args.character.count("-") > 1:
            raise Exception("Invalid range")
        elif (args.character.count("-") == 1) and (args.character[0] == "-"):
            # this is negative number, most probably
            starting = int(args.character)-1
        elif (args.character.count("-") == 1) and (args.character[0] != "-"):
            starting = int(args.character.split("-")[0]) - 1
            ending = int(args.character.split("-")[1])
        else:
            #probably just a single numeric here
            starting = int(args.character) - 1


        with open(args.FILE, 'r') as f:
            for line in f:
                if ending is None:
                    print(line[starting])
                else:
                    print(line[starting:ending])


    print(output)


if __name__ == '__main__':
    run_job()