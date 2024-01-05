#!/usr/bin/env python
# https://leetcode.cn/problems/container-with-most-water/

import unittest
from typing import List


def max_area(height: List[int]) -> int:
    """先全遍历：
    左边界逐次右移，每次移动后进入运算；运算过程中，右边界从左边界开始逐次移动至右末端。
    然后剪枝：
    左边界右移时，剪去不必要的进入。
    右边界改为从右末端向左边界靠拢。
    右边界向左边界靠拢时，剪去不必要的靠拢，中途就可以停止。
    """

    height_len = len(height)

    if height_len <= 1:
        raise ValueError

    left, right = 0, height_len - 1
    container_height = min(height[left], height[right])
    result = container_height * (height_len - 1)
    while left < right:
        left_height = height[left]

        if left_height > container_height:
            while right > left:
                right_height = height[right]
                if right_height > container_height:
                    container_height = min(left_height, right_height)
                    result = max(result, container_height * (right - left))

                    if right_height >= left_height:
                        break

                right -= 1

        left += 1

    return result


class TestContainerWithMostWater(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(2, max_area([1, 2, 1]))

    def testStandard(self):
        self.assertEqual(49, max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def testPyramid(self):
        top = 1000
        left = [i for i in range(top)]
        right = left[::-1]

        self.assertEqual(500000, max_area(left + [top] + right))


if __name__ == "__main__":
    unittest.main()
