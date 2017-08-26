import argparse


def run_job():
    parser = argparse.ArgumentParser()
    # parser.add_argument("dir", nargs='?', default="/usr/local/",
    #                     help="optionally provide location where the find should take place")
    # parser.add_argument("-f", "--file", help="grep on file contents", required=False)
    # parser.add_argument("-p", "--print", help="print matching locations", required=False)
    parser.add_argument("-e", "--REGEX", help="match based on regex", required=False)
    parser.add_argument("FILE", help="grep on file contents")
    args = parser.parse_args()

    if (args.FILE is not None and
            args.REGEX == ''):
        with open(args.FILE, 'r') as f:
            print(f.read())


if __name__ == '__main__':
    run_job()