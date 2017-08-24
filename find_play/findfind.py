import argparse
import re
import os



def run_job():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", nargs='?', default="/usr/local/",
                        help="optionally provide location where the find should take place")
    parser.add_argument("-n", "--name", help="find name by regex", required=False)
    parser.add_argument("-p", "--print", help="print matching locations", required=False)
    args = parser.parse_args()

    for item in os.listdir(args.dir):
        if re.search(args.name, item):
            print("{}/{}".format(args.dir,item))

if __name__ == '__main__':
    run_job()