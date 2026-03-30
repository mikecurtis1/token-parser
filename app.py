# ---- CLI ENTRY POINT ----

import sys

from token_parser import TokenParser, Token

def main():
    if len(sys.argv) > 1:
        q = ' '.join(sys.argv[1:])
    else:
        q = sys.stdin.read().strip()

    tokenizer = TokenParser()
    tokens = tokenizer.tokenize(q)

    for t in tokens:
        print(t)


if __name__ == "__main__":
    main()
