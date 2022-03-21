# mips-autoformat
MIPS autoformatter, indent MIPS code and comments automatically.

## Usage
`python3 autoformat.py [-h] [-f FILE] [-l LEFT] [-r RIGHT]`

## Optional Arguments:
```
  -h, --help              show this help message and exit
  -f FILE, --file FILE    file to autoindent
  -l LEFT, --left LEFT    left margin
  -r RIGHT, --right RIGHT right margin
```
## Note
Defaults to formatting all `*.s` files if no `--file` argument provided.
