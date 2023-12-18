#!/usr/bin/env python
from __future__ import annotations

import math
import random
import re
import string
import time
import unittest
import uuid


class ULID:
    """
    Inspired by https://g.co/bard/share/18866036c6ca and https://github.com/ulid/spec.
    Main feature is distributed and sortable.
    Use 32-based number system, [0-9a-v], 5 bits per character, case-insensitive
    Format: "timestamp_bits-worker_bits-random_bits"
    Random_bits are default to 48-bit, worker_bits are default to 16-bit, the rest are timestamp bits.
    ULID bits are limited by N-bit computer, but under uuid compatibility, they're 128 bits.
    """

    digits = string.digits + string.ascii_lowercase[:22]
    base_bits = 5
    timestamp_bits = 64
    worker_bits = 16
    rand_bits = 48
    mask = pow(2, base_bits) - 1
    rand = random.SystemRandom()
    parse_pattern = re.compile("^(\w+)-(\w+)-(\w+)$")

    __timestamp_length = math.ceil(timestamp_bits / base_bits)
    __worker_length = math.ceil(worker_bits / base_bits)
    __rand_length = math.ceil(rand_bits / base_bits)

    @staticmethod
    def parse(ulid: str) -> ULID:
        matches = ULID.parse_pattern.match(ulid)
        if not matches:
            raise ValueError(f"Unrecognized {ulid=}")

        new_id = ULID(0)
        new_id.timestamp_millis, new_id.worker_id, new_id.rand_num = (ULID.unsigned_int_from_32base(x)
                                                                      for x in matches.group(1, 2, 3))

        return new_id

    @staticmethod
    def parse_uuid(uuid_str: str) -> ULID:
        uuid_bits = bin(uuid.UUID(uuid_str).int)

        new_id = ULID(0)
        new_id.rand_num = int(uuid_bits[-ULID.rand_bits:], 2)

        uuid_bits = uuid_bits[:-ULID.rand_bits]
        new_id.worker_id = int(uuid_bits[-ULID.worker_bits:], 2)

        uuid_bits = uuid_bits[:-ULID.worker_bits]
        new_id.timestamp_millis = int(uuid_bits, 2)

        return new_id

    @staticmethod
    def unsigned_int_to_32base(n: int) -> str:
        assert n >= 0

        number = ""
        while True:
            index = n & ULID.mask
            number = ULID.digits[index] + number

            n = n >> ULID.base_bits
            if 0 == n:
                break

        return number

    @staticmethod
    def unsigned_int_from_32base(txt: str) -> int:
        base = ULID.mask + 1
        return sum([ULID.digits.index(v) * pow(base, i) for i, v in enumerate(txt.lower()[::-1])])

    def __init__(self, worker_id, rand: random.Random = None):
        if worker_id < 0:
            raise ValueError(f"{worker_id=} should not be negative")

        self.worker_id = worker_id
        self.timestamp_millis = int(time.time() * 1000)
        self.rand_num = (rand or ULID.rand).randint(0, pow(2, ULID.rand_bits) - 1)

    def __repr__(self):
        return f"ULID({self.worker_id})"

    def __str__(self):
        ts = ULID.unsigned_int_to_32base(self.timestamp_millis).rjust(ULID.__timestamp_length, "0")
        worker = ULID.unsigned_int_to_32base(self.worker_id).rjust(ULID.__worker_length, '0')
        r = ULID.unsigned_int_to_32base(self.rand_num).rjust(ULID.__rand_length, '0')

        return f"{ts}-{worker}-{r}"

    def __eq__(self, other):
        return isinstance(other, ULID) \
            and self.timestamp_millis == other.timestamp_millis \
            and self.worker_id == other.worker_id \
            and self.rand_num == other.rand_num

    def uuid(self) -> uuid.UUID:
        rand_bytes = self.rand_num.to_bytes(int(ULID.rand_bits / 8), byteorder="big")
        worker_bytes = self.worker_id.to_bytes(int(ULID.worker_bits / 8), byteorder="big")
        ts_bytes = self.timestamp_millis.to_bytes(len(rand_bytes) + len(worker_bytes), byteorder="big")

        return uuid.UUID(ts_bytes.hex() + worker_bytes.hex() + rand_bytes.hex())

    def value(self):
        ts = ULID.unsigned_int_to_32base(self.timestamp_millis)
        worker = ULID.unsigned_int_to_32base(self.worker_id)
        r = ULID.unsigned_int_to_32base(self.rand_num)

        return f"{ts}{worker}{r}"


class TestULID(unittest.TestCase):
    def testBasic(self):
        arr = ["a", "0"]
        arr.sort()
        self.assertEqual(["0", "a"], arr)

        arr = ["1", "0"]
        arr.sort()
        self.assertEqual(["0", "1"], arr)

        arr = ["d", "a"]
        arr.sort()
        self.assertEqual(["a", "d"], arr)

        arr = ["a", "ab"]
        arr.sort()
        self.assertEqual(["a", "ab"], arr)

        ulid = ULID(15000)
        print(ulid, "|", ulid.uuid(), "|", ulid.value())

        ulid = ULID(random.randint(0, 65535))
        print(ulid, "|", ulid.uuid(), "|", ulid.value())

    def testPerformance(self):
        worker_id = random.randint(0, 65535)
        turns = 1000000

        start = time.time_ns()
        for _ in range(turns):
            ULID(worker_id)

        elapsed = (time.time_ns() - start) / 1000000

        print(f"{elapsed:.3f} ms elapsed for generating {turns} ULID, {turns / (elapsed / 1000):.0f} id/s.")

    def testUnsignedIntFrom32base(self):
        self.assertEqual(15000, ULID.unsigned_int_from_32base("eko"))
        self.assertEqual(0x3a98, ULID.unsigned_int_from_32base("eko"))

    def testEquality(self):
        src = ULID(500)
        dest = ULID.parse(str(src).upper())

        self.assertTrue(src == dest)

    def testParseUUID(self):
        ulid = ULID(15000)
        new_id = ULID.parse_uuid(str(ulid.uuid()))
        self.assertEqual(ulid, new_id)


if __name__ == "__main__":
    unittest.main()
