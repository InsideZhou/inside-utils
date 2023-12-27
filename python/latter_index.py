#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random
import string


def latter_index(chars: str) -> (str, int, int):
    alphabet = string.ascii_lowercase
    chars_lower = chars.lower()

    char, distance = "", None

    for c in chars_lower:
        d = alphabet.index(c)
        d = min(d, 25 - d)
        if distance is None or d < distance:
            char, distance = c, d

    return chars, char, alphabet.index(char) + 1 if distance is not None else None, distance


if "__main__" == __name__:
    parser = argparse.ArgumentParser(description="字符串中距字母序列两端最近的字母")
    parser.add_argument('chars', nargs='?', type=str, default="")
    args = parser.parse_args()

    txt = args.chars
    if len(args.chars) == 0:
        txt = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in
            range(random.randint(3, 5)))

    print(latter_index(txt))
