import argparse

import re


def run_job():
    parser = argparse.ArgumentParser()
    # parser.add_argument("dir", nargs='?', default="/usr/local/",
    #                     help="optionally provide location where the find should take place")
    # parser.add_argument("-f", "--file", help="grep on file contents", required=False)
    # parser.add_argument("-p", "--print", help="print matching locations", required=False)
    parser.add_argument("-e", "--REGEX", help="match based on regex", required=False)
    parser.add_argument('-v', action='store_true', help="return inverted match")
    parser.add_argument("FILE", help="grep on file contents")
    args = parser.parse_args()

    output = ''

    if (args.FILE is not None and
            args.REGEX == ''):
        with open(args.FILE, 'r') as f:
            output = f.read()

    if (args.FILE is not None and
                args.REGEX != ''):
        with open(args.FILE, 'r') as f:
            for line in f.readlines():
                regex = args.REGEX
                invert = args.v
                checker = re.search(regex, line) if not invert else not re.search(regex, line)

                if checker:
                    output += line

    print(output)


if __name__ == '__main__':
    run_job()