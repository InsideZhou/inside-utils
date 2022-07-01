#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string, random, argparse

DEFAULT_LENGTH = 16

if "__main__" == __name__:
	parser = argparse.ArgumentParser(description="随机字符串生成器")
	parser.add_argument('length', nargs='?', type=int, default=DEFAULT_LENGTH, help=f"随机字符串的长度，默认{DEFAULT_LENGTH}。")

	args = parser.parse_args()

	txt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(args.length))
	print(txt)
