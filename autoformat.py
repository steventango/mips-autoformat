import argparse
import fileinput
import glob
import re

def autoformat(file_name: str, left_margin: int, right_margin: int):
    min_left = 0
    lefts = []

    with open(file_name) as f:
        for line in f:
            split = line.split('# ')
            if len(split) != 2 or len(split[0].strip()) == 0:
                lefts.append(-1)
            else:
                left = len(split[0].rstrip())
                lefts.append(left)
                min_left = max(min_left, left)

    with fileinput.FileInput(file_name, inplace=True) as f:
        for line, left in zip(f, lefts):
            line = line.rstrip()
            if left == -1:
                print(line)
            else:
                if all(c not in line for c in ['.', ':']):
                    delta = len(line)
                    content = line.lstrip()
                    delta -= len(content)
                    line = ' ' * left_margin + content
                    left += left_margin - delta

                indented = re.sub(
                    r'[ \t]+# ',
                    ' ' * ((min_left - left) + right_margin) + '# ',
                    line
                )
                print(indented)

def main():
    parser = argparse.ArgumentParser(description='MIPS Autoformater')
    parser.add_argument('-f', '--file', help='file to autoformat')
    parser.add_argument('-l', '--left', help='left margin', default=2)
    parser.add_argument('-r', '--right', help='right margin', default=4)
    args = parser.parse_args()
    if args.file:
        autoformat(args.file, args.left, args.right)
    else:
        files = glob.glob('*.s')
        for file in files:
            autoformat(file, args.left, args.right)


if __name__ == '__main__':
    main()
