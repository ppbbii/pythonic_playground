import argparse

parser = argparse.ArgumentParser()
parser.add_argument("files", help="files to be cat'ed", nargs='+')
parser.add_argument("-o", "--output", help="redirect stream to a file", required=False)
args = parser.parse_args()

def process_file_line(file):
    if args.output:
        with open('{}'.format(args.output), 'a') as w:
            for line in f:
                w.write(line + '\n')
                print(line)

for a in args.files:
    try:
        with open(a, 'r') as f:
            process_file_line(f)

    except OSError:
        print("File not found!")