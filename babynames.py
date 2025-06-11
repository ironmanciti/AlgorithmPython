import sys
import re

def extract_name(filename):
    """Extracts rank and baby names from the given HTML file."""
    names = []
    # use "with" to ensure the file is closed properly
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # the rank can be more than one digit so use \d+ instead of \d
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    for rank, boy, girl in tuples:
        names.append((rank, boy, girl))
        print(rank, boy, girl)

    return names

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print("file 명 미입력")
        sys.exit(1)
    filename = './babynames/' + args[0]
    extract_name(filename)
