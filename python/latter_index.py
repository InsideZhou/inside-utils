#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random
import string


def latter_index(chars: str) -> (str, int, int):
    alphabet = string.ascii_lowercase
    chars_lower = chars.lower()

    result, char, distance = [], "", None

    for c in chars_lower:
        idx = alphabet.index(c)
        d = min(idx, 25 - idx)

        result.append(f"{c}({idx + 1},{d})")

        if distance is None or d < distance:
            char, distance = c, d

    return " ".join(result), alphabet.index(char) + 1


if "__main__" == __name__:
    parser = argparse.ArgumentParser(description="字符串中距字母序列两端最近的字母")
    parser.add_argument('chars', nargs='?', type=str, default="")
    parser.add_argument('mod', nargs='?', type=int, default="7")
    args = parser.parse_args()

    txt, mod = args.chars, args.mod
    if len(args.chars) == 0:
        txt = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in
            range(random.randint(3, 5)))

    result = latter_index(txt)
    print(txt, result[0], f"{result[1]}%{mod}={result[1] % mod}")
