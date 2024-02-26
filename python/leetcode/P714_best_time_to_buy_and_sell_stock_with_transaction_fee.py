#!/usr/bin/env python
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
import unittest
from typing import List


# 这个递归重复计算太多，且由于递归过深导致栈溢出。
def max_profit(prices: List[int], fee: int) -> int:
    def calc_profit(price_list: List[int]) -> int:
        list_length = len(price_list)
        if list_length <= 1:
            return 0

        profit = max(price_list[-1] - price_list[0] - fee, 0)

        for i in range(1, list_length):
            profit = max(calc_profit(price_list[:i]) + calc_profit(price_list[i:]), profit)

        return profit

    return calc_profit(prices)


# 仅遍历一次，在每个价格负差处判断是否应该以之前的区间完成一次交易。
def max_profit_2(prices: List[int], fee: int) -> int:
    profits = []

    lowest, highest = prices[0], prices[0]
    for i in range(1, len(prices)):
        current = prices[i]
        if highest <= current:
            highest = current
            continue

        if highest - current > fee:
            profit = highest - lowest - fee
            if profit > 0:
                profits.append(profit)

            lowest, highest = current, current

        if current < lowest:
            lowest, highest = current, current

    if highest - lowest > fee:
        profits.append(highest - lowest - fee)

    return sum(profits)


class TestBestTimeToBuyAndSellStockWithTransactionFee(unittest.TestCase):
    def test0(self):
        self.assertEqual(4, max_profit([1, 2, 3, 4, 5, 6], 1))
        self.assertEqual(4, max_profit_2([1, 2, 3, 4, 5, 6], 1))

    def test1(self):
        self.assertEqual(8, max_profit([1, 3, 2, 8, 4, 9], 2))
        self.assertEqual(8, max_profit_2([1, 3, 2, 8, 4, 9], 2))

    def test2(self):
        self.assertEqual(6, max_profit([1, 3, 7, 5, 10, 3], 3))
        self.assertEqual(6, max_profit_2([1, 3, 7, 5, 10, 3], 3))

    def test3(self):
        self.assertEqual(13, max_profit([1, 4, 6, 2, 8, 3, 10, 14], 3))
        self.assertEqual(13, max_profit_2([1, 4, 6, 2, 8, 3, 10, 14], 3))

    def test4(self):
        self.assertEqual(4, max_profit_2([2, 1, 4, 4, 2, 3, 2, 5, 1, 2], 1))


if __name__ == '__main__':
    unittest.main()
