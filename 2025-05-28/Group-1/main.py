#!/usr/bin/env python3
# ^ this means that you can `chmod +x` this file and then ./<this_file>
# will just run this file as if it were python :)

# TODO:
#   get diffed files (subprocess?)
#       - set config
#       - no colour
#   run a regex on the diff
#       - each file
#       - is (start of string) ^ a new line or start of file
#           + start of line please
#           + $ is end of line
#   print a good error message
#   return 0 or 1

import re
import subprocess
import sys

def get_diff() -> str:
    result = subprocess.run(
        ["git", "diff", "--staged", "-U0", "--raw", "--no-color", "--word-diff=none", "--find-renames"], 
        capture_output=True)
    return result.stdout.decode("utf-8")

def do_regex(regex_pattern: re.Pattern, text: str | None = None) -> re.Match[str] | None:
    text = text or get_diff()
    for line in text.splitlines():
        if line.startswith("-"):
            continue
        line = line.removeprefix("+")
        if match := re.match(regex_pattern, line):
            return match
    return None

def main() -> None:
    """check diff for problems and raise if so """
    if do_regex(re.compile("import itertools")):
        print("bad", file=sys.stderr)
        sys.exit(1)
    print("good", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    print("running ")
    main()

# ln -s main.py ../../.git/hooks/diffregex.py